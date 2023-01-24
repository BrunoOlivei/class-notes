```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="assets/css/reset.css">
    <link rel="stylesheet" href="grid.css">
</head>
<body class="corpo">
    <header class="cabecalho"></header>
    <nav class="lateral"></nav>
    <section class="meio"></section>
    <section class="direita-cima"></section>
    <section class="direita-baixo"></section>
</body>
</html>
```

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.corpo {
    background-color: #444444;
    padding: 16px;
    width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr;
    gap: 16px;
}

.cabecalho {
    background-color: #cc2a2a;
    border-radius: 10px;
    min-width: 50px;
    min-height: 50px;
    grid-column: span 4;
}

.lateral {
    background-color: #45cc2a;
    border-radius: 10px;
    min-width: 50px;
    min-height: 50px;
    grid-row: span 3;
}

.meio {
    background-color: #2aa6cc;
    border-radius: 10px;
    min-width: 50px;
    min-height: 50px;
    grid-column: span 2;
    grid-row: span 3;
}

.direita-cima {
    background-color: #352acc;
    border-radius: 10px;
    min-width: 50px;
    min-height: 50px;
}

.direita-baixo {
    background-color: #cc2a96;
    border-radius: 10px;
    min-width: 50px;
    min-height: 50px;
    grid-row: span 2;
}

```

