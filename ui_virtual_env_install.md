@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ git . add;git commit -m 'updates';git push
git: '.' is not a git command. See 'git --help'.

The most similar commands are
        am
        gc
        mv
        p4
        rm
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   compile_video.py
        modified:   generate_scene.py
        modified:   requirements.txt
        modified:   scenes.yaml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .vscode/
        formula_leanardo.ai

no changes added to commit (use "git add" and/or "git commit -a")
Everything up-to-date
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ git add .;git commit 
-m 'updates';git push
[main 4cc71f2] updates
 Author: Erdem <rifaterdemsahin@gmail.com>
 7 files changed, 260 insertions(+), 40 deletions(-)
 create mode 100644 .vscode/arm_toolchain.json
 create mode 100644 .vscode/settings.json
 create mode 100644 formula_leanardo.ai
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 2 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 4.93 KiB | 4.93 MiB/s, done.
Total 10 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/rifaterdemsahin/leonardoai
   f7ce55c..4cc71f2  main -> main
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ git . add;git commit 
-m 'updates';git push
git: '.' is not a git command. See 'git --help'.

The most similar commands are
        am
        gc
        mv
        p4
        rm
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        environment.md
        setup_env.sh

nothing added to commit but untracked files present (use "git add" to track)
Everything up-to-date
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ git . add;git commit -m 'updates';git push
git: '.' is not a git command. See 'git --help'.

The most similar commands are
        am
        gc
        mv
        p4
        rm
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        environment.md
        setup_env.sh

nothing added to commit but untracked files present (use "git add" to track)
Everything up-to-date
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ git add .;git commit 
-m 'updates';git push
[main 5d68bf6] updates
 Author: Erdem <rifaterdemsahin@gmail.com>
 3 files changed, 127 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 environment.md
 create mode 100644 setup_env.sh
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 2.56 KiB | 1.28 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/rifaterdemsahin/leonardoai
   4cc71f2..5d68bf6  main -> main
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ chmod +x setup_env.sh
@rifaterdemsahin ➜ /workspaces/leonardoai (main) $ ./setup_env.sh
Requirement already satisfied: pip in ./.venv/lib/python3.12/site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/29/a2/d40fb2460e883eca5199c62cfc2463fd261f760556ae6290f88488c362c0/pip-25.1.1-py3-none-any.whl.metadata
  Downloading pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-25.1.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 23.7 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1
Successfully installed pip-25.1.1
Collecting moviepy
  Downloading moviepy-2.2.1-py3-none-any.whl.metadata (6.9 kB)
Collecting PyYAML
  Downloading PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Collecting leonardo-ai-sdk
  Downloading leonardo_ai_sdk-6.5.1-py3-none-any.whl.metadata (25 kB)
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting python-dotenv
  Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)
Collecting decorator<6.0,>=4.0.2 (from moviepy)
  Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
Collecting imageio<3.0,>=2.5 (from moviepy)
  Downloading imageio-2.37.0-py3-none-any.whl.metadata (5.2 kB)
Collecting imageio_ffmpeg>=0.2.0 (from moviepy)
  Downloading imageio_ffmpeg-0.6.0-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting numpy>=1.25.0 (from moviepy)
  Downloading numpy-2.3.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting proglog<=1.0.0 (from moviepy)
  Downloading proglog-0.1.12-py3-none-any.whl.metadata (794 bytes)
Collecting pillow<12.0,>=9.2.0 (from moviepy)
  Downloading pillow-11.2.1-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (8.9 kB)
Collecting tqdm (from proglog<=1.0.0->moviepy)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Collecting eval-type-backport>=0.2.0 (from leonardo-ai-sdk)
  Downloading eval_type_backport-0.2.2-py3-none-any.whl.metadata (2.2 kB)
Collecting httpx>=0.28.1 (from leonardo-ai-sdk)
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting pydantic>=2.10.3 (from leonardo-ai-sdk)
  Downloading pydantic-2.11.5-py3-none-any.whl.metadata (67 kB)
Collecting python-dateutil>=2.8.2 (from leonardo-ai-sdk)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting typing-inspect>=0.9.0 (from leonardo-ai-sdk)
  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
Collecting anyio (from httpx>=0.28.1->leonardo-ai-sdk)
  Downloading anyio-4.9.0-py3-none-any.whl.metadata (4.7 kB)
Collecting httpcore==1.* (from httpx>=0.28.1->leonardo-ai-sdk)
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.28.1->leonardo-ai-sdk)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.10.3->leonardo-ai-sdk)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.33.2 (from pydantic>=2.10.3->leonardo-ai-sdk)
  Downloading pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting typing-extensions>=4.12.2 (from pydantic>=2.10.3->leonardo-ai-sdk)
  Downloading typing_extensions-4.14.0-py3-none-any.whl.metadata (3.0 kB)
Collecting typing-inspection>=0.4.0 (from pydantic>=2.10.3->leonardo-ai-sdk)
  Downloading typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->leonardo-ai-sdk)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect>=0.9.0->leonardo-ai-sdk)
  Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting sniffio>=1.1 (from anyio->httpx>=0.28.1->leonardo-ai-sdk)
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Downloading moviepy-2.2.1-py3-none-any.whl (129 kB)
Downloading decorator-5.2.1-py3-none-any.whl (9.2 kB)
Downloading imageio-2.37.0-py3-none-any.whl (315 kB)
Downloading pillow-11.2.1-cp312-cp312-manylinux_2_28_x86_64.whl (4.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 34.2 MB/s eta 0:00:00
Downloading proglog-0.1.12-py3-none-any.whl (6.3 kB)
Downloading PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (767 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 767.5/767.5 kB 11.8 MB/s eta 0:00:00
Downloading leonardo_ai_sdk-6.5.1-py3-none-any.whl (154 kB)
Downloading requests-2.32.4-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Downloading urllib3-2.4.0-py3-none-any.whl (128 kB)
Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)
Downloading certifi-2025.4.26-py3-none-any.whl (159 kB)
Downloading eval_type_backport-0.2.2-py3-none-any.whl (5.8 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading imageio_ffmpeg-0.6.0-py3-none-manylinux2014_x86_64.whl (29.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 29.5/29.5 MB 61.8 MB/s eta 0:00:00
Downloading numpy-2.3.0-cp312-cp312-manylinux_2_28_x86_64.whl (16.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 73.9 MB/s eta 0:00:00
Downloading pydantic-2.11.5-py3-none-any.whl (444 kB)
Downloading pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 76.4 MB/s eta 0:00:00
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading typing_extensions-4.14.0-py3-none-any.whl (43 kB)
Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Downloading typing_inspection-0.4.1-py3-none-any.whl (14 kB)
Downloading anyio-4.9.0-py3-none-any.whl (100 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Installing collected packages: urllib3, typing-extensions, tqdm, sniffio, six, PyYAML, python-dotenv, pillow, numpy, mypy-extensions, imageio_ffmpeg, idna, h11, eval-type-backport, decorator, charset_normalizer, certifi, annotated-types, typing-inspection, typing-inspect, requests, python-dateutil, pydantic-core, proglog, imageio, httpcore, anyio, pydantic, moviepy, httpx, leonardo-ai-sdk
Successfully installed PyYAML-6.0.2 annotated-types-0.7.0 anyio-4.9.0 certifi-2025.4.26 charset_normalizer-3.4.2 decorator-5.2.1 eval-type-backport-0.2.2 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.10 imageio-2.37.0 imageio_ffmpeg-0.6.0 leonardo-ai-sdk-6.5.1 moviepy-2.2.1 mypy-extensions-1.1.0 numpy-2.3.0 pillow-11.2.1 proglog-0.1.12 pydantic-2.11.5 pydantic-core-2.33.2 python-dateutil-2.9.0.post0 python-dotenv-1.1.0 requests-2.32.4 six-1.17.0 sniffio-1.3.1 tqdm-4.67.1 typing-extensions-4.14.0 typing-inspect-0.9.0 typing-inspection-0.4.1 urllib3-2.4.0
✅ Virtual environment created and packages installed.
Use `source .venv/bin/activate` to start the environment.