# transformaciones y transiciones
1. transform
2. transition
3. animation

### transform
tranformar elementos
1. transform
2. transform-origin
3. transform-style
4. perspective
5. perspective-origin
6. backface-visibility

### transition
movimiento entre A y B
1. transition
2. transition-property
3. transition-duration
4. transition-timing-function(optional)
5. transition-delay (optional)

### animation
cambios de propiedades en el transcurso del tiempo 
1. animation
2. animation-name
3. animation-duration 
4. animation-timing-function (optional)
5. animation-delay (optional)
6. animation-iteration-count (optional)
7. animation-direction (optional)
8. animation-fill-mode (optional) 
9. animation-play-state (optional)

# transform
### sintaxis y sus propiedades
transform: none | transform-funtions | initial | inherit;

# pseudo-clases
1. a:link   {color:red} ***color del link***
2. a:visited    {color:lime} ***visitado***
3. a:hover    {color:tomato} ***mouse sobre el elemento***
4. p:not(.maravillas)   {color:fucsia} ***excluye el elemento con la clase maravillas***

# pseudo-elementos
1. div::before{content: ":)" } ***elementos antes del elemento*** 
1. div::after{content: ":(" } ***elementos despues del elemento*** 

# timing functions
Planos y ejes 

x,y,z

### aceleraciones y desaceleraciones
podemos ver en cubic-bezier.com mas fromas de acelerar y desacelerar elementos

cubic-bezier(.47,.83,.74,.29)

### contexto de apilamiento

# tranformaciones 2D y 3D
### sintaxis 
- transform: none | transform-functions | initial | inherit
- transform: tranform

|tipo|trasladar|escalar|rotar|inclinar|matriz|perspectiva|
|---|---|---|---|---|---|---|
|Múltiple | translate()| scale()| rotate() | skew() | matrix() | perspective() |
|Eje X| translateX() | scaleX() | rotateX() | skewX() |
|Eje Y| translateY() | scaleY() | rotateY() | skewY() |
|Eje Z| translateZ() | scaleZ() | rotateZ() | 
|3D | translate3d() | scale3D() | rotate3D()| |matrix3D|

1. transform: scale(1.5)
2. transform: skew(1.2)
3. transform: rotate(deg)


