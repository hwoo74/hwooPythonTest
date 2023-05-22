1. 참고 URL
    - https://wikidocs.net/8
    - https://wikidocs.net/book/4170    
    - https://wikidocs.net/book/5445

2. 설치.
    - python 설치.
        - http://www.python.org/downloads 윈도우용 다운로드.
        - Add python.exe to PATH" 옵션을 반드시 선택하여 설치. 
        - python3 명렁어로 실행 ... ( python 은 python2.7 이 실행됨... )
    - 에디터 
        - https://www.jetbrains.com/pycharm/download/
        - https://dora-guide.com/pycharm-install/
            - 설치방법.
            - 체크할꺼 체크, 재부팅은 나중에 해도 됨.
            - 실행후 Setting > Project > Python Interpreter 선택해서, 
                - 선택하고 저장. 
    - 아나콘다 설치.
        - 아나콘다로 갈꺼면 처음부터 이쪽을 참고해서.. 
        - https://tibetsandfox.tistory.com/36
        - 머신러닝이나 데이터 분석 등에 사용하는 여러가지 패키지가 기본적으로 포함되어있는 파이썬 배포판
        - 파이선 설치했다면, 지우고 설치해야 충돌을 피할수 있음.. 
    - jupiter notebook ..
        - ???
3. 실행.
    - 시작메뉴에서 선택 실행 하거나 ..
    - 에디터에서 실행시키세유 ... ;; 

4. venv 폴더 
    - 프로젝트 별로 독룁된 실행환경 구성 처리용 디렉토리. 
    - https://www.daleseo.com/python-venv/
    - 파이썬 3.3 부터는 venv 모듈이 기본적으로 포함
    - 실행
        ```
        $ cd <프로젝트 디렉터리>
        $ python -m venv .venv
        $ ls -a
        .     ..    .venv
        ```
    - pycharm 에디터에서는 자동으로 실행해 주는듯. 
    - git 에 포함되어야 설치 라이브러리가 뭔지 알 수 있음 ... 허나, 개별 pc 설정이라 .. 다운받아도 안먹힐 수 있음 ... 
    - 따라서, 해당 venv 보단... requirements.txt 파일에 라이브러리를 공유하는 방식을 씀.

5. .idea 폴더
    - https://wotres.tistory.com/entry/idea-%ED%8F%B4%EB%8D%94%EB%9E%80-gitignore-%EC%B6%94%EA%B0%80%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0
    - 프로젝트별 설정값 저장. .gitignore 에 추가해 둬야 함.

6. package 설치 방법 ....
    - pip 으로 관리. 
        - PyPI - 파이선 패키지 등록 싸이트. https://pypi.org/
        - pip help
            - 설치확인/ 도움말/ 
            - 최신버전은 pip도 자동 설치됨.
    - package install example 
        - pypi 사이트에서 bubblesort 검색해서 찾아봄 ... 
        ```
        prompt> pip install bubblesort
        Collecting bubblesort
        Downloading bubbleSort-0.1.0-py3-none-any.whl (1.3 kB)
        Installing collected packages: bubblesort
        Successfully installed bubblesort-0.1.0

        [notice] A new release of pip available: 22.3.1 -> 23.1.1
        [notice] To update, run: python.exe -m pip install --upgrade pip
        ```
        - 사용법을 모르니 venv\Lib\...\__init__.py 를 열어봄.
    - 패키지 배포...
        - https://velog.io/@devmin/python-freeze-packages-tip
        - pip freeze > requirements.txt
            - 해당 명령어로 .. 패키지를 백업해 두고, 
        - pip install -r requirements.txt
            - 이걸로 복구 (r 은 read 약자)
        - 멀쩡하게 설치된 라이브러리를 못찾을때, 이방식으로 pyCharm 에서 업데이트 하니 돌아간다 ..... 