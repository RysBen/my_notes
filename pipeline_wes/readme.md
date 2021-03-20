# 1. Basic
## shell

## WDL, CWL
```bash
cwl-runner input.cwl input-job.yaml
```

```yaml
#!/usr/bin/env cwl-runner

cwlVersion: V1.0
class: CommandLineTool
bashCommand: echo
inputs:
  para_flag:
    type: boolean
    inputBinding:
      position: 1
      prefix: -f
  para_int:
    type: int
    inputBinding:
      position: 3
      prefix: --int
      separate: false
  para_file:
    type: File?
    inputBinding:
      position: 2
      prefix: --file=
      separate: false
outputs: []
```

```yaml
para_flag: true
pare_int: 666
para_file:   # File类型需要给定 class 和 path 字段
  class: File
  path: text.txt
```


# 2. Pipeline and enige
## Shell

## Make

## Snakemake

## Nextflow

## Bpipe

## Argo

## Cromwell(WDL)
