# MCP Agent Tutorial

## 개요
MCP(Machine Conversation Protocol) Agent는 LLM과 외부 도구를 연결하는 방법을 학습하기 위한 튜토리얼입니다. 이 프로젝트는 MCP를 사용하여 날씨 정보를 제공하는 서버와 LangGraph를 활용한 에이전트 구축 방법을 다룹니다.

## 시작하기

### 사전 요구사항
- Python 3.8 이상
- Anaconda/Miniconda (권장)
- LangChain, LangGraph, MCP 라이브러리

### 설치 방법
```bash
# 가상환경 생성 및 활성화
conda create -n mcp-agent python=3.12
conda activate mcp-agent

# 필요 패키지 설치
pip install langchain langchain-mcp-adapters langgraph mcp langchain-google-genai python-dotenv
```

## 주요 구성 요소

### 1. MCP-HandsOn.ipynb
- MCP와 LangGraph를 활용한 에이전트 구축 튜토리얼 노트북
- 다양한 통신 방식(SSE, Stdio)을 통한 MCP 서버 연결 방법
- Google Gemini 모델을 활용한 에이전트 개발

### 2. mcp_server_local.py
- 로컬 환경에서 실행 가능한 MCP 서버
- 날씨 정보를 제공하는 간단한 도구(tool) 구현
- FastMCP를 활용한 서버 구성 예제

### 3. mcp_server_rag.py (개발 중)
- RAG(Retrieval-Augmented Generation) 기능을 갖춘 MCP 서버
- 문서 처리 및 검색 기능 구현

## 사용 방법

### MCP 서버 실행
```bash
# 터미널에서 가상환경 활성화 후 실행
conda activate mcp-agent
python mcp_server_local.py
```

### 튜토리얼 실행
1. Jupyter Notebook 실행
2. MCP-HandsOn.ipynb 파일 열기
3. 노트북의 안내에 따라 셀 실행

## 추가 예정 기능
- RAG 기반 에이전트 구축
- 다중 도구 연동 에이전트 구성
- 프로덕션 환경 배포 가이드

## 참고 자료
- [LangGraph MCP Agents](https://github.com/teddynote-lab/langgraph-mcp-agents)
- [Machine Conversation Protocol (MCP) 문서](https://mcp.ai)