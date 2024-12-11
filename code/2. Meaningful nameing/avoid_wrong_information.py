# 직각삼각형의 빗변(hypotenuse) 를 사용 할 때, hp 가 훌륭한 약자처럼 보여도 유닉스의 변종을 의미하기 떄문에 혼동을 일으킬 수 있다.

# 비슷한 예시로, 여러계정을 그룹으로 묶을 때, 실제로 List 가 안리ㅏ면 accountList 라는 이름을 사용하지 말아라. 프로그래머에게 List 는 
# 계정을 담는 컨테이너가 실제 List 가 아니라면 accountGroup 이나 bunchOfAccounts 등의 명명으로 List 를 사용하지 않는다.
# -- 실제 List -- 라도 이름안에 컨테이너 유형의 이름을 담지 않는 것이 바람직하다 .


## 흡사한 이름을 사용하지 않도록 한다 .
## 어떤 모듈에서 XYZControllerEfficientHandlingOfString 이라는 이름을 사용하고 조금 멀리 떨어진 모듈에서 XYZ ControllerForEfficientStroageOfString
## 이라는 이름을 사용한다면, 둘의 차이를 알아차리기힘들다. 하나씩 읽어봐야한다. 


###끔찍한 예제
a = 1
if O == 1:
    a = O1
else:
    l = Ol

    