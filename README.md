"# Python_game"

<h1>Math_Hopscotch</h1>

Player1, Player2 두명이 함께 방향키를 사용하여 플레이 하는 게임.

초록색 땅에 도착하면 운에 따라 점수가 크게 + 될 수도, - 될 수도 있다.

우측에 각 플레이어의 점수를 색으로 구분하고,

현재 누구의 차례인지, 지금이 총 몇 번째 차례인지
쉽게 알 수 있도록 표시했으며,

하단에는 승리 조건을 출력했다.
(1P/2P 중 한명이라도 오른쪽 끝에 도착하면 게임 종료,
게임 종료 시점에서 Score가 더 높은 Player가 승리.)

------------------------------------------------------------------------------------------------------------
<image src = "https://user-images.githubusercontent.com/88473185/186391993-c4ebfd11-b108-4055-87e7-ffebebfec883.png" width="200" height="400"/>

각 칸마다 랜덤으로 1~10사이의 정수를 갖는 9x9의 땅을 생성.

땅의 각 행에서(초록색 땅이 위/아래 한쪽으로 쏠리는 경우 방지) 랜덤하게 1칸을 초록색 땅으로 변경.

왼쪽 상단, 하단에 각각 Player1, Player2 생성.

------------------------------------------------------------------------------------------------------------

1P 먼저  시작하고 방향키 중 하나를 누르면,
 자신이 누른 방향으로 이동하고 해당 칸에 적혀있는 숫자만큼
 자신의 Score에 더한 후 상대 차례로 넘어감.

※만약 누른 방향이 벽이라면 움직이지 않고 자신의 차례만 넘어감.

------------------------------------------------------------------------------------------------------------

초록색 땅에 도착하면 해당 칸에 적혀있는 숫자에 -3 ~ 3 까지의 정수 중 
랜덤으로 곱하고 그것을 현재 Player의 점수에 더한다.

ex) 우측 이미지에서 2P는 10의 값을 갖는 칸에 랜덤값이 +2가 나와서 
Score에 20 (10 x 2)을 더해 1P와 큰 격차를 벌렸다.
(점수 증감: -30~30)

우측 하단에 "BGM Option" 버튼을 클릭하면 BGM을 On/Off 할 수 있다.
(다른 효과음들은 그대로)

------------------------------------------------------------------------------------------------------------

Player가 이미 지나간 칸은 값이 0인 빨간색 땅으로 변경해서,
높은 점수의 칸에만 계속 머무는 것을 방지했다.

1P / 2P 둘 중 한명이 오른쪽 끝까지 도착하면 게임 종료,
게임 종료 시점에서 더 높은 점수를 갖고 있는 사람이 승리한다.

메세지 박스로 이긴 사람, 각 Player의 점수를 표시하고,
"예" 버튼을 누르면 게임을 처음부터 다시 시작한다

------------------------------------------------------------------------------------------------------------

차별성: 얼핏 보면 간단해 보이는 게임이지만, 랜덤으로 생성되는 땅에서 최대 Score를 얻고 게임을 끝내기 위한 동선을 계산해야 하며,

초록색 칸을 만듦으로써 처음에 생성된 땅이 자신에게 유리하지 못하더라도 극복할 수 있는 여지와, "-" 값이 더해졌을 때의 변수를 주었고, 

상대방보다 우월한 Score를 갖고 있다면 우측 끝으로 빠르게 이동해 게임을 끝내는 것을 목표로 플레이 하는 등 심리전적인 요소도 있어

짧은 PlayTime에 비해 질리지 않고 반복해서 재밌게 Play가 가능하기 때문에 간단한 내기를 하기에 매우 좋은 게임이다.

느낀점: pygame을 이용해 9x9칸을 만들고, 각 칸 안에 값을 집어넣어 플레이어가 이동할 수 있도록 하는 부분이 생각한 것보다 간단하지 않아 개발하는 과정이 재미있었고, 

for문을 사용할 때 함축을 이용하면 코드가 간단해지지만 조건이 많이 붙을 경우 오히려 함축을 사용하지 않는 것이 알아보기 더 편했고,

클래스와 함수들을 잘 사용하면 코드가 얼마나 간결해지는지 크게 느꼈다.
