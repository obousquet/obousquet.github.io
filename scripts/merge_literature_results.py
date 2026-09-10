#!/usr/bin/env python3
"""Combine exact duplicate extraction sections with provenance; retain differing claims."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from research_library import library_root, records


def sections(text):
    context=[]; body=[]
    for line in text.splitlines():
        heading=re.match(r'^(#{1,6})\s+(.+)',line)
        if heading:
            if body and '\n'.join(body).strip():
                yield ' / '.join(label for _,label in context),'\n'.join(body).strip()
            body=[]; level=len(heading.group(1))
            context=[item for item in context if item[0]<level]
            context.append((level,heading.group(2)))
        else:body.append(line)
    if body and '\n'.join(body).strip():
        yield ' / '.join(label for _,label in context),'\n'.join(body).strip()


def merge(root):
    stats={'papers_with_merged_results':0,'input_sections':0,'unique_sections':0,
           'duplicate_source_files_linked':0,'duplicate_source_bytes':0}
    for record in records(root):
        packet=root/record['path']
        documents=[]
        for name in ('key-results.md','notes.md'):
            if (packet/name).exists():documents.append(packet/name)
            documents.extend(sorted((packet/'variants').glob('**/'+name)))
        if len(documents)>1:
            blocks={}
            for document in documents:
                relative=document.relative_to(packet).as_posix()
                for heading,body in sections(document.read_text(encoding='utf-8',errors='replace')):
                    stats['input_sections']+=1
                    normalized=re.sub(r'\s+',' ',body).strip()
                    block=blocks.setdefault(normalized,{'body':body,'sources':[]})
                    block['sources'].append((heading,relative))
            if blocks:
                lines=['# Merged result extractions','',
                       'Identical section text appears once below. Differing statements and project',
                       'interpretations are retained separately; this merge does not resolve conflicts.',
                       'Each excerpt links to its original extraction and section context.','']
                for i,block in enumerate(blocks.values(),1):
                    heading = block['sources'][0][0] or 'Extraction'
                    lines += [f'## {heading} ({i})','']
                    for heading,relative in block['sources']:
                        lines.append(f'- [{heading or "Source extraction"}]({relative})')
                    lines += ['',block['body'],'']
                (packet/'merged-results.md').write_text('\n'.join(lines),encoding='utf-8')
                stats['papers_with_merged_results']+=1;stats['unique_sections']+=len(blocks)
        # Only deduplicate immutable extracted sources within the same paper.
        # Editable notes and metadata must remain independent.
        seen={}
        candidates=sorted(packet.rglob('*'),key=lambda p:('variants' in p.parts,len(p.parts),str(p)))
        for path in candidates:
            if not path.is_file() or path.is_symlink():continue
            if path.suffix not in ('.txt','.tex','.html'):continue
            if not path.name.startswith(('source','original')):continue
            data=path.read_bytes();digest=hashlib.sha256(data).hexdigest()
            if digest in seen:
                temporary=path.with_name(f'.{path.name}.dedupe-{os.getpid()}')
                temporary.symlink_to(os.path.relpath(seen[digest],path.parent));temporary.replace(path)
                stats['duplicate_source_files_linked']+=1;stats['duplicate_source_bytes']+=len(data)
            else:seen[digest]=path
    return stats


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path)
    args=parser.parse_args();print(json.dumps(merge(library_root(args.root)),indent=2))

if __name__=='__main__':main()
