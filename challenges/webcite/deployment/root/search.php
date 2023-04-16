<!doctype html>
<html lang="en">

<?php include 'db.php';?>
<?php
if(!isset($_GET["q"])) {
  //nothing
}
else {
    // select query
    //todo
}
?>

<head>
    <?php include 'head.php';?>
    <title>search - webcite</title>
</head>
<body>
    <nav>
    <?php include 'nav.php';?>
    </nav>

    <main>
        <article>
            <h1>Search Query:</h1>
            <form>
            <input type="text" name="search" placeholder="search" aria-label="search" required>
            <button type="submit" onclick="event.preventDefault();//todo">search</button>
            </form>
        </article>
    </main>

    <footer>
    <?php include 'foot.php';?>
    </footer>
  </body>

</html>