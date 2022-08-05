>## 1번
### **어려웠던 점**  
 01번은 사실 이전에 데일리 실습에서 한 내용이기 때문에 쉬울거라 생각했습니다. 하지만 1번이 가장 까다로웠습니다.  

  부트스트랩에서 navbar를 가져왔지만, 먼저 상단의 navbar에 logo.png를 삽입하여 다른 항목들과 정렬하는 부분에서 조금 애를 먹었습니다. 이후에 width 768px이상에서 navbar의 home, community, login까지 나타나고 width 768px미만에서 사라지게 하는 부분에서 다시 막혔습니다. 이를 navbar 에서 'expend-lg'에서 'lg'부분을 'md'로 수정하여 해결하였습니다.  
하지만 01번에서 가장 많은 시간을 잡아먹은 부분은 Login 클릭 시 Modal을 출력하는 부분이었습니다. Modal 자체는 bootstrap에서 가져왔지만, 그 'login'을 누른 경우 Modal이 뜨지 않는 문제가 발생하였고, 이를 교수님께 질문하여 'button' 태그의 data-bs-toggle="modal" data-bs-target="#login" 부분을 'modal fade'클래스가 있는 div에서 id= login으로 설정해야 Modal창이 뜬다고 하셔서 이를 그대로 반영하여 문제를 해결하였습니다.

>## 2번
### **어려웠던 점**
02번 home.html의 앞부분인 bootstrap carousel component에서 그대로 가져와 이미지 주소만 넣으면 해결 됐기 때문에 체감상 01번 보다는 쉬웠습니다. 하지만 scetion 내부의 card component에서 문제가 발생하였습니다. bootstrap에서 가져오는 것 까지는 문제가 없었지만, 이후에 576px미만인 경우와 576px이상인 경우에 한 행에 표시되는 카드 수를 달리 할당하는 것에서 막혔고, 이를  **'col-12 col-md-4'**  즉, 총 12칸으로 할당하고 만약 md 사이즈이하가 된다면 4칸을 차지하도록 하여 해결하였습니다.

>## 3번
### **어려웠던 점**
03번은 개인적으로 가장 복잡했던 것 같습니다. bootstrap에서 Aside(게시판 목록)과 Section(게시판)을 가져오는 것은 역시나 쉬웠지만, 이를 배치하는 부분에서 막혔습니다. title인 'Community'와  Aside와 Section을 하나로 묶어 배치하다 보니 가로로 했을 경우 3가지가 모두 한 줄에 들어오는 문제가 발생하였기에 이를 하나의 'container'에 묶은 이후 div.d-flex 바깥으로 'Community'를 빼고, Aside와 Section을 하나씩 차지하게 한 이후 정렬을 하여 이를 해결하였습니다. 마지막 문제로 viewport가 992px 이상일 경우에 bootstrap tables content로 구성되어 HTML 요소 영역 기준 우측 5/6만큼의 너비를 가지게 하는 부분에서 막혔고, 이를 해결하기 위해 viewport의 가로 크기가 992px 미만일 경우에 HTML article요소로 표시될 부분을 따로 만들어 992px 이상에서는 보이지 않게 설정하고, 992미만에서 보이도록 설정하여 문제를 해결하였습니다.



