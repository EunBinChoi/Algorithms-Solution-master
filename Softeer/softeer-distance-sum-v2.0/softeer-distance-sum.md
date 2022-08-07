## [21년 재직자 대회 본선] 거리 합 구하기
- 난이도 3/5
- 정답률 25.95%
- https://softeer.ai/practice/info.do?idx=1&eid=635

### 문제
현호는 사내 네트워크 분석 업무를 담당하게 되었다.  
현재 사내 네트워크는 N개의 노드를 가지는 트리 형태의 네트워크인데, 이 말은 두 노드간의 연결이 정확히 N-1개 있어서 이 연결만으로 모든 노드간에 통신을 할 수 있다는 뜻이다.  

각 노드에 1에서 N사이의 번호를 붙이면 i번째 연결은 xi번 노드와 yi번 노드를 양방향으로 연결하며, 통신에 걸리는 시간은 ti이다.   
D(i,j)는 i번 노드와 j번 노드 사이의 거리를 나타내는데, i번 노드에서 여러 연결을 거쳐 j번 노드에 도달하기 위해 걸리는 최소 시간이다.  

노드를 들를 때 추가적인 작업이 없는 이상적인 시간을 따진다. 현호는 네트워크 분석을 위해 어떤 노드 i를 기준으로 다른 모든 노드 사이와의 거리의 합을 알고 싶다.   
즉, <img src="https://latex.codecogs.com/svg.image?\sum_{j=1}^{N}D(i,&space;j)" title="\sum_{j=1}^{N}D(i, j)" />을 알고 싶다.  

입력예제 2번을 예로 들면, 다음과 같이 7개의 노드로 이루어진 네트워크로 표현할 수 있다.   
각 연결 위에 적힌 수는 t를 나타낸다.  

### 제약조건
- 1 ≤ N ≤ <img src="https://latex.codecogs.com/svg.image?2\times&space;10^{5}" title="2\times 10^{5}" />
- 주어진 N-1개의 연결로 모든 노드가 연결되어 있다.
- 1 ≤ <img src="https://latex.codecogs.com/svg.image?x_{i}&space;" title="x_{i} " />, <img src="https://latex.codecogs.com/svg.image?y_{i}&space;" title="y_{i} " /> ≤ N
- 1 ≤ <img src="https://latex.codecogs.com/svg.image?t_{i}&space;" title="t_{i} " /> ≤ <img src="https://latex.codecogs.com/svg.image?10^{6}" title="10^{6}" />

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
- 첫 번째 줄에 노드의 개수 N이 주어짐
- 다음 N-1줄의 i번째 줄에는 i번째 연결을 나타내는 세 정수 <img src="https://latex.codecogs.com/svg.image?x_{i}&space;" title="x_{i} " />, <img src="https://latex.codecogs.com/svg.image?y_{i}&space;" title="y_{i} " />, <img src="https://latex.codecogs.com/svg.image?t_{i}&space;" title="t_{i} " />가 주어짐
  
### 출력형식
- N개의 줄에 걸쳐서, 
- i번째 줄에는 i번 노드와 다른 모든 노드 사이의 거리의 합, <img src="https://latex.codecogs.com/svg.image?\sum_{j=1}^{N}D(i,&space;j)" title="\sum_{j=1}^{N}D(i, j)" />를 출력한다.

### 입력예제1
4  
1 2 1  
2 3 2  
3 4 4  

### 출력예제1
11  
9  
9  
17  

### 입력예제2
7  
1 2 5  
1 3 2  
1 4 8  
3 5 4  
3 6 1  
4 7 6  

### 출력예제2
38  
63  
40  
62  
60   
45   
92  