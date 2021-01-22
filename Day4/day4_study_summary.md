---
layout: post
title: Day4
hide_title: False
excerpt: BoostCamp AI Tech - DAY 4
author: Song
tags: [BoostCamp, AI, Day4]
---

# Day 4

### 진행 사항
  - [x] 파이썬 기초 문법 III
      - [x] <Assignment> morsecode
      - [x] Python Object Oriented Programming
      - [x] Moudle and Project
  - [x] Peer Session
  - [x] Pandas 개인 공부
  - [x] Markdown 찍먹


## 학습 내용
---
Day4에서 제공된 강의에선 OOP의 개념과 특성, 모듈과 패키지 그리고 프로젝트에 대해 배울 수 있었습니다.

과제가 별도로 출제되었고, 이는 Morse <-> Alphabet 상호변환을 지원하는 프로그램 작성이었습니다.

또한 개인 공부로 Pandas data frame의 col/row 추가 삭제 및 정렬을 공부하였으며 지금 Markdown 언어를 찍먹해보고 있습니다.

### **Special Thanks To**
### 마크다운으로 작성된 Day3 정리 자료를 공유해준 동료 부스트캠퍼 **박재우**

<br/>
<br/>
<br/>


## 오늘의 학습정리 내용 
<br/>

---
## (개인적으로) Python Object Oriented Programming 에서 중요하거나 어려웠던 것
---

### 1. 클래스 이름은 CamelCase로 작성한다.
~~~python
class ClassName(상속받는 개체명)
~~~
<br/>

### 2. 언더바 두 개 (__)는 특수한 예약 함수나 함수명 변경 **맨글링**으로 사용합니다. ex) str, add 등..
<br/>

### 3. Class에 Method를 추가할때는 반드시 인자로 self를 넘겨주어야 합니다. 
<br/>

### 4. Python에서의 Private 선언법
~~~python
class Students(object):
   def __init__(self) :
      self.__name #이렇게 언더바를 사용하여 private 선언을 합니다.
~~~
+ private 걸린 것을 @property를 이용하여 풀어줄 수 있다.
<br/>
<br/>

### 5. Inner Function & Decorator
~~~python
def plus(func):
    def inner(*args, **kwargs):
        print(args[1] * 30 + kwargs["one"])
        func(*args, **kwargs)
        print(args[1] * 30 + kwargs["one"])
    return inner

@plus #이렇게 Decorator를 이용하여, Inner function을 쉽게 사용할 수 있다.
def printer(msg, marks, *args, **kwargs) :
    print(msg)
printer("Hello", "+", one = "DOH") 
~~~
+ 이 외에, @Generator_power(2) 예시도 참고해볼 법 하다. 이 경우, gnerator_power 함수에 (2)가 붙게 되고, 그 밑에 있는 하위 wrapper 함수가 @generator_power 밑에 선언된 함수를 인자로 받아 inner_function이 작동된다.
<br/>
<br/>
<br/>

---
## Module and Project (별거 없었음)
---


### 1. 모듈, 패키지, 프로젝트의 기본 개념
모듈은 보통 py 파일이며, 패키지는 모듈과 \_\_init\_\_.py 를 담고있으며, 패키지가 모여 프로젝트가 된다.
<br/>프로젝트 폴더는 \_\_main\_\_.py를 지닌다. 프로젝트 폴더명으로 실행 가능하다.
~~~cmd
python .\프로젝트 폴더
~~~
<br/>
<br/>

---
## Morsecode 과제 고찰
---
### 1. 문자열 사이에 있는 두 개 이상의 공백 처리에 다음과 같은 정규식 표현 사용
~~~python
import re
pattern = re.compile(r'\s\s+')
morse_sentence = re.sub(pattern, '  ', morse_sentence) #두 개 이상의 공백들이, 두개의 공백으로 변환된다.
~~~
+ 지나고보니 안 써도 됐었지만 어쨌든 .. 정규식을 나중에 공부해봐야겠다.
<br/>

### 2. list comprehension을 이용하여 다음과 같이 조건이 더해진 리스트를 빠르게 만들수 있다.
~~~python
new_eng_list = [ch for ch in new_eng_st if ch.isalpha() or ch.isdigit() == True or ch == " "]
~~~
<br/>

### 3. dict에 현재 찾는 값이 없는지 알아볼 때 다음과 같은 표현 사용
~~~python
if find_val not in get_morse_code_dict().values() :
~~~
+ values를 keys()로 바꾸면 key도 찾을 수 있다.
<br/>

#### 이번 과제는 string을 다뤄보는 과제였다고 정리할 수 있겠다.
<br/>
<br/>
<br/>

---
## Pandas 개인 공부
---
### 1. Col 추가
~~~python
df['full_name'] = df['first'] + ' ' + df['last'] #이렇게 기존 col 이용하여 추가.
df[['first','last']] = df['full_name'].str.split(" ", expand=True) #이렇게 기존 col을 대체하며 추가.
~~~
<br/>

### 2. Col 삭제
~~~python
df.drop(columns=['first','last'])
~~~
<br/>

### 3. Row 추가
~~~python
df.append({dict}, ignore_index=True) #직접 값 dict 타입으로 입력해서 추가하기
df.append(other_df, ignore_index=True, sort=False) #다른 df와 merge 하기. _inplace나 assign이 필요하다.
~~~
<br/>

### 4. Row 삭제
~~~python
#인덱스를 알고 있을 경우
.drop(index = 원하는 row의 인덱스)
#혹은 filter를 이용하여
filt = df['last'] == "Song"
df.drop(index = df[filt].index) #한 줄에 쓸수도 있지만 이렇게 써야 가독성이 좋다.
~~~
<br/>

### 5. Sort
~~~python
df.sort_values(by='last') # by와 추가 파라미터 ascending은 list형태로 넘겨줄 수도 있음, inplace 변경 적용시 필요
#혹은
df['last'].sort_values()

#위 방법은 df의 다른 col value를 포함하여 출력하고, 밑의 방법은 'last' col 값만 출력한다.

df.nlargest(개수) #랭킹처럼 상위 10
df.nsmallest(개수) #하위 10
~~~
<br/>
<br/>
<br/>

---
## Peer Session
---
### 1. remove()와 discard()의 차이
#### remove()의 경우, 없으면 error를 뱉어내지만 discard()의 경우 넣어준 값이 없어도 그냥 넘어가므로 있으면 안되는 놈을 확인사살할때 유용하게 쓰일 수 있다.
<br/>

### 2. numpy 공부자료 확보
#### 향후 numpy를 많이 사용할것 같은데, 공부할 유투브 자료 링크를 확보해놓았다.
https://www.youtube.com/watch?v=mirZPrWwvao
<br/>
<br/>
<br/>

---
## Markdown 찍먹
---
### 결론 :
+ 장점 : 파이썬 코드가 아주 보기 좋게 작성되고 나중에 보기 깔끔하다. 
<br/>

+ 단점 : 아직 깔끔하게 써내는데 익숙치 않아 학습정리의 내용에 집중하기가 어려웠고, 시간이 많이 소요되었다.
<br/>

나중에 블로그를 하게되면 쓰기 좋아보이지만 시간 소요를 생각해 보았을 때 블로그를 운영하지 않는다면 굳이? 라는 생각이 들긴 함 ...
<br/>
하지만 정말 확실하게 장담할수 있는 것은 **HTML**을 썼을때보단 쓰기 쉬웠다는것
<br/>
오늘의 원래 방식 학습정리 링크 : https://drive.google.com/file/d/1E43Tyhe_8x6kMY0f44EY6qI7HtdTjCds/view?usp=sharing
