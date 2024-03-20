## [21년 재직자 대회 본선] 비밀 메뉴2
- 난이도 3/5
- 정답률 20.73%
- https://softeer.ai/practice/info.do?idx=1&eid=633

### 문제
회사 식당에는 전설처럼 전해 내려오는 비밀 메뉴에 대한 소문이 있다. 소문의 내용은 대강 이러하다.  
식권 자판기의 버튼을 특정 순서대로 누르고 결제를 하면, 평소와는 다른 색깔의 식권이 나온다.   
이 식권을 배식대에 제출하면, 어떤 비밀 메뉴를 받을 수 있다는 것이다.  

물론 이를 실제로 본 사람은 아무도 없어서, 어떤 메뉴가 나오는지는 커녕 눌러야 하는 버튼의 순서조차 알려져 있지 않다.  
식당의 평범한 이용객인 당신은 이 소문을 들은 순간 비밀 메뉴에 호기심이 생겼다.  
그 실체를 쫓아 연구를 거듭한 지도 어언 몇 달째. 당신은 자판기의 버튼을 아무렇게나 두들기면서, 비밀 메뉴가 나오는 조작법을 두 가지 찾아냈다!  

당신은 이 두 조작법을 연구해 비밀 메뉴 조작법을 찾고자 한다.  
당신은 버튼에 1 이상 K 이하의 정수로 된 번호를 매겨, 이러한 숫자의 나열로 버튼 조작을 표현했다.   
당신의 직감은 둘 모두에 포함된 일련의 조작법 중 가장 긴 것을 찾아야 한다고 말하고 있다.  

일련의 조작법이란, 나열된 숫자들에 존재하는 연속된 부분 수열을 의미한다.  
길이가 각각 N과 M인 버튼 조작 과정이 주어질 때, 둘 모두에 완전히 포함되는 일련의 조작 과정 중 가장 긴 것의 길이를 출력하여라.  

### 제약조건
- 1 ≤ N ≤ 3,000
- 1 ≤ M ≤ 3,000
- 1 ≤ K ≤ 1,000,000
- 각 버튼의 번호는 1 이상 K 이하

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
- 첫째 줄에 N, M, K가 공백을 사이에 두고 주어짐.
- 둘째 줄에 첫 번째 버튼 조작을 나타내는 N개의 정수가 공백을 사이에 두고 주어짐.
  - 각 정수는 1 이상 K 이하
- 셋째 줄에 두 번째 버튼 조작을 나타내는 M개의 정수가 공백을 사이에 두고 주어짐.
  - 각 정수는 1 이상 K 이하
  
### 출력형식
- 비밀 메뉴 조작법으로 가능한 가장 긴 것의 길이를 첫째 줄에 출력함.
- 만일 겹치는 조작이 전혀 없다면 0을 출력함.

### 입력예제1
3 4 4  
2 3 1  
3 1 4 2  

### 출력예제1
2  

두 조작 모두에 등장하는 수열은 다음과 같다:  
[1],[2],[3],[3 1]  

이중 가장 긴 것은 [3 1]이며 그 길이는 2이다. 따라서 첫째 줄에 2를 출력한다.  

### 입력예제2
4 10 3  
2 1 3 2  
1 3 2 1 3 2 1 3 2 1   

### 출력예제2
4  

첫 번째 조작인 [2 1 3 2]가 두 번째 조작에 온전히 등장하므로, 그 길이인 4가 곧 답이 된다.  

### 입력예제3
5 4 9  
3 1 4 1 5  
9 8 7 6  

### 출력예제3
0

두 조작에 겹치는 것이 하나도 없으므로 답은 0이다.  