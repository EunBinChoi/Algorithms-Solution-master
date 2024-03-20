## 8단 변속기
- 난이도 2/5
- 정답률 64.84%
- https://softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=76922

### 문제
현대자동차에서는 부드럽고 빠른 변속이 가능한 8단 습식 DCT 변속기를 개발하여 N라인 고성능차에 적용하였다. 
관련하여 SW 엔지니어인 당신에게 연속적으로 변속이 가능한지 점검할 수 있는 프로그램을 만들라는 임무가 내려왔다. 

당신은 변속기가 1단에서 8단으로 연속적으로 변속을 한다면 ascending, 8단에서 1단으로 연속적으로 변속한다면 descending, 둘다 아니라면 mixed 라고 정의했다. 변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면 mixed인지 출력하는 프로그램을 작성하시오.  

### 제약조건
- 주어지는 숫자는 문제 설명에서 설명한 변속 정도이며, 1부터 8까지 숫자가 한번씩 등장함.

--------------------------------------------------------

#### 복잡도
- 시간 복잡도 - 알고리즘 수행 시간
- 공간 복잡도 - 알고리즘의 메모리 사용량

#### 시간 복잡도
- 코딩 테스트 문제의 시간제한은 대략 5초
- python이 초당 2천만번 연산이 가능하다고 가정하는 것이 좋음 (5초에 1억번) (20,000,000 == 2*10^7)

<code><b>시간제한이 1초인 문제를 만났을 떄, 일반적인 기준은 다음과 같음:</b></code>
- N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 2,000인 경우: 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 해결할 수 있음

#### 연산 횟수에 따른 시간 복잡도
- 연산 횟수가 5억
- C언어 - 1 ~ 3초
- python - 5 ~ 15초 (pypy는 때떄로 C보다 빠름)

#### 파이썬의 자료구조
- list, tuple: O(n) (선형 순회)
- set, dict: O(1) ~ O(n) 
(hash를 통해 저장하므로 접근시간은 O(1), 단 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)

--------------------------------------------------------

### 입력형식
- 첫째 줄에 8개 숫자가 주어짐.
  
### 출력형식
- 첫째 줄에 ascending, descending, mixed 중 하나를 출력함.

### 입력예제1
1 2 3 4 5 6 7 8  

### 출력예제1
ascending