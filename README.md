# Custom_TO_CLothes_DLC
[스파르타코딩클럽 내일배움캠프 AI 3기] A4팀 딥러닝 프로젝트
## 프로젝트 소개
기본적으로 입고 다니는 옷들을 내가 좋아하는 필터를 이용해서 커스텀 된 옷을 주문하는 쇼핑몰을 기획하였습니다.  
내가 커스텀한 옷들을 볼 수 있고, 커스텀 된 다른 사용자의 옷들을 인기 순위별로 볼 수 있습니다.

## 개발기간
2022.11.22 ~ 2022.11.28
## front-end github-address
[Custom_To_Clothes_DLC_Frontend](https://github.com/marinred/Custom_To_Clothes_DLC_Frontend)

## 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" align='left'/>
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white" align='left'/>
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white" align='left'>
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" align='left'>
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" align='left'>
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white" align='left'><br>


## 역할 파트
- **front-end** :
  - 회원가입, 로그인, 로그아웃: 임동근님
  - 커스텀제작: 이태규님
  - 옷프로필 : 염보미님
  - 메인페이지, 프로필페이지: 주세민님
  - 장바구니, 주문완료 리스트: 정진엽님
- **back-end** :
  - 회원 가입, 로그인, 로그아웃: 임동근님
  - 커스텀 제작: 이태규님, 염보미님
  - 메인 페이지, 프로필 페이지: 주세민님
  - 옷프로필, 장바구니, 주문완료 리스트: 정진엽님
- **Deep Learning** :
  - 이태규님(옷 제작 시스템)
  - 염보미님(옷 제작 시스템)
  
## 주요 기능
1. 회원 가입 / 로그인
    - 회원 가입
    - 로그인
    - 프로필   
2. 메인페이지
    - 좋아요순으로 커스텀 내용 공개하는 기능
    - 커스텀제작페이지 이동하는 기능
3. 프로필페이지
    - 현재 로그인 되어있는 사용자 이름 + 안녕하세요 출력하는 기능
    - 커스텀한 옷 목록보여주는 기능
4. 디자인제작 페이지
    - 디자인할 옷종류 선택, 디자인할 시안 선택 기능
    - 선택한 데이터를 제작 완료페이지로 이동하는 기능  
5. 제작완료 페이지(주문페이지)
    - 주문할 옷 사이즈, 수량 선택 기능
6. 장바구니페이지
    - 주문할 옷 가격, 수량, 사이즈 출력 기능
7. 주문목록페이지
    - 주문한 옷 가격, 수량, 사이즈, 상태 출력 기능
   
    
## 와이어프레임
https://www.figma.com/file/2wXsZhQlOURcWATyJzz2he/Untitled?node-id=0%3A1&t=1Sm22iCgAOGjt3Sy-0
![Figma](https://user-images.githubusercontent.com/112370211/204183124-1c8f9175-e3b6-49a4-bb6d-fed04774f3df.png)


## DB 설계
![DB](https://user-images.githubusercontent.com/112370211/204172591-0b4f8b0a-481b-49ae-abb5-b72deec6caf2.jpg)

## API 설계
| App | 기능 | URL | Method | Request | Response |
| --- | --- | --- | --- | --- | --- |
| User |  |  |  |  |  |
|  | 회원가입 | /user/signup/ | POST | {“email”,“username”,“password”,”password2”} | status:200<br>"result": "ok" |
|  | 로그인 | /user/api/token/ | POST | {“email”, “password”} |  |
|  | 로그아웃 | /user/logout/ |  |  |  |
|  | 프로필 | /user/<int:user_id>/ | GET |  | {"id", "article_image"} |
|  | 메인페이지 | / | GET |  | {"id", "article_image", "likes_count"} |
| Article |  |  |  |  |  |
|  | Base 정보 | /article/| GET |  | {“draft”, "style"} |
|  | 커스텀 제작 | /article/ | POST | {"draft_id", "style_image", "style_id"} | {“article”} |
|  | 커스텀 제적 수정 | /article/ | PUT | {"article_id", "draft_id", "style_image", "style_id"} | {“article”} |
|  | 게시글 좋아요 | /<int:article:id>/like/| POST | {"article_id"} | {"좋아요 등록(취소) 완료"} |
| Order |  |  |  |  |  |
|  | 장바구니 조회 | /order/ | GET |  | {"id", "article_user", "mount", "size", "price"} |
|  | 주문하기 | /order/<int:article_id>/ | POST | {"size", "mount", "status"} | {"order"} |
|  | 주문목록 | /order/ | GET |  | {"id", "article_user", "mount", "size", "price"} |  |

## 딥러닝 모델
[style-transfer-pytorch](https://github.com/crowsonkb/style-transfer-pytorch)

## 프로젝트 시연영상
![image](https://user-images.githubusercontent.com/113073174/204188971-949176c9-1b0e-471b-90e2-c257f54d5ac9.png)
!프로젝트 시연영상](https://www.youtube.com/watch?v=dH_CHanu6E4)

