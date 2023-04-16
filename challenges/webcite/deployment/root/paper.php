<!doctype html>
<html lang="en">

<?php include 'db.php';?>
<?php
if(!isset($_GET["doi"])) {
  die();
}
// select query
$sql = $conn->prepare('SELECT * FROM papers WHERE doi = ?');
$sql->bind_param("s", $in_doi);
$in_doi = $_GET["doi"];
$sql->execute();

$sql->bind_result($id, $title, $doi);
while ($data = $sql->fetch()) {
    $papers[] =  (object)['title' => $title, 'doi' => $doi];
}

if(!isset($papers)) {
    die();
}
$paper = $papers[0];
?>

<head>
    <?php include 'head.php';?>
    <title>paper - webcite</title>
</head>
<body>
    <nav>
    <?php include 'nav.php';?>
    </nav>

    <main>
<?php
// foreach ($users as $user) {
    echo "<article>";
    echo "title: " . $paper->title;
    echo "<br/>";
    echo "DOI: " . $paper->doi;
    echo "</article>";
// }
?>
    </main>

    <footer>
    <?php include 'foot.php';?>
    </footer>
  </body>

</html>