# SSAFYWork

[![GitHub Repo](https://img.shields.io/badge/GitHub-SSAFYWork-blue?logo=github)](https://github.com/ChessPark0613/SSAFYWork)

**SSAFYWork** 레포지토리는 SSAFY 활동 중 진행되는 여러 프로젝트/스터디/자료들을 관리하기 위한 레포.  


---

## 📂 레포지토리 구조
```

SSAFYWork/
├── live/          # 라이브 코딩 강의
├── aps\_basic/     # 알고리즘 기본 강의
├── web/           # 웹 관련 강의
└── ...            # 추가 서브모듈

````

각 디렉터리는 **Git Submodule**로 관리되며, 독립적인 레포지토리를 참조함.

---

## 🔗 레포지토리
- GitHub: [https://github.com/ChessPark0613/SSAFYWork](https://github.com/ChessPark0613/SSAFYWork)

---

## 🚀 서브모듈 관리
### 서브모듈 초기화 및 최신화
```bash
git submodule update --init --recursive --remote
```

* `--init` : 서브모듈 초기화
* `--recursive` : 중첩된 서브모듈까지 포함
* `--remote` : 원격 브랜치 최신 커밋으로 업데이트

### 상태 확인
```bash
git submodule status
```

앞에 `+` 기호가 붙은 경우 → 서브모듈이 최신 커밋보다 뒤쳐져 있는 상태입니다.

---

* 새로운 서브모듈을 추가할 경우:

```bash
git submodule add <repo-url> <path>
```