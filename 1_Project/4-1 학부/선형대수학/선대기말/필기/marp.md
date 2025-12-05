<!-- $theme: gaia -->
<!-- $size: A4 -->

# Marp

#### kanziw

---
<!-- page_number: true -->

## Cover

* 가운데에 Title 이 나오기 위해선 `#` or `>` 으로만 작성되어야 한다.

#### Theme

* theme 은 현재 2가지만 지원한다.
```md
<!-- $theme: default --> or <!-- $theme: gaia -->
```
* default 는 Cover 에서 title 이 가운데 정렬이 되지 않는다.
* 그리고 폰트 크기도 작다.
* 직접 theme 를 건드리기 전 까진 gaia 를 쓰는 것으로...

---
## Cover

#### Page

* Cover 에는 페이지를 감추기 위해 2p 에 아래의 옵션을 준다.
```md
<!-- page_number: true -->
```

---
## Size

* size 는 `4:3` 이 default 이며, `16:9`, `A0`-`A8`, `B0`-`B8` 을 지원한다.
* `-portrait` 을 붙이면 세로로 사이즈가 설정된다.
* 아래처럼 사용할 수 있다.
```
<!-- $size: A4 -->
```

---
## Size

* `$width` 와 `$height` 를 직접 설정할 수도 있다.
* 단위는 default 로 px 를 사용하며, `cm`, `mm`, `in`, `pt`, `pc` 를 사용할 수 있다.
```md
<!--
$width: 12in
$height: 12in
-->
```

---
<!--
$theme: gaia
*template: invert
-->

## Template

#### invert
* 색이 반전된다.
* $theme: gaia 에서만 적용된다.
```md
<!--
$theme: gaia
template: invert
-->
```

---
<!--
$theme: gaia
*template: gaia
-->

## Template

#### gaia
* gaia 라는 template 이 적용된다.
* $theme: gaia 에서만 적용된다.
```md
<!--
$theme: gaia
template: gaia
-->
```
* 특정 슬라이드에만 효과를 적용하기 위해선 `*` 을 사용한다.
* ex) `<!-- *template: gaia -->`

---
## Image
![70% center](./kanziw.png)
```md
![70% center](./kanziw.png)
```
* x% 로 이미지의 비율을 결정할 수 있다.
* 위치는 center 만 적용된다.

---
## Image
#### Background
![bg 30%](./kanziw.png)
```md
![bg 30%](./kanziw.png)
```
* bg : 배경이미지 적용
* x% : 이미지 비율
* original : 투명 효과 제거

---
## Effects

#### Bold
* **Bold** sample
```md
**Bold** sample
```

#### Italic
* *Italic sample*
```md
*Italic sample*
```
* `*` 대신 `_` 로 감싸도 Italic 이 적용된다.

---
## Effects

#### Bold + Italic
* **BOLD *Italic***
```md
**BOLD *Italic***
```

#### Cancel
* ~~Cancel line~~
```md
~~Cancel line~~
```

---
## Effects

#### Block
* `Block`  
```md
`Block`
```
* \` 3개씩으로 앞뒤를 감싸면 Code block 을 작성할 수 있다.
\```js
\```
* 위처럼 Code block 에 어떤 종류의 글이 적히는지 명시하면 Code highlight 가 적용되기도 한다.

---
## Effects

#### 인용
> 인용 sample
```md
> 인용 sample
```

#### small
<small>small sample</small>
```md
<small>small text</small>
```

---
## Effects

#### Highlight
* ==Highlight== sample
```md
==Highlight== sample
```
* Here is <span style="background-color:yellow;">yellow marker highlight</span> !!
```md
Here is <span style="background-color:yellow;">yellow marker highlight</span> !!
```

---
## Effects

#### Emoji
* :arrow_right: :arrow_left: :arrow_up: :arrow_down: :smile:
```md
:arrow_right: :arrow_left: :arrow_up: :arrow_down: :smile:
```

---
## Etc

#### Footer
<!-- *footer: this is a footer -->
```md
<!-- *footer: this is a footer -->
```
* 이 슬라이드 이후의 좌하단에 footer 가 보여진다.

#### Prerender
```md
<!-- prerender: true -->
```
* 고용량의 이미지 로딩 등의 이유로 슬라이드를 미리 render 해야 할 필요가 있을 때 사용한다.

---
## Etc

#### Maths Typesetting

* `KaTeX` 를 이용해 수학 수식을 표시한다. 
* $ax^2+bc+c$
```md
$ax^2+bc+c$
```
* $$I_{xx}=\int\int_Ry^2f(x,y)\cdot{}dydx$$
```md
$$I_{xx}=\int\int_Ry^2f(x,y)\cdot{}dydx$$
```

---
## 출처

* [Marp](https://yhatt.github.io/marp/)
* Basic example [Slide](https://speakerdeck.com/yhatt/marp-basic-example) / [Code](https://raw.githubusercontent.com/yhatt/marp/master/example.md)
* Gaia example [Slide](https://speakerdeck.com/yhatt/introducing-marps-gaia-theme) / [Code](https://github.com/yhatt/marp/blob/master/examples/gaia.md)