<!doctype html>
<html lang="en">

<?php include 'db.php';?>
<?php
if(!isset($_GET["name"])) {
  die();
}
// select query
$sql = 'SELECT * FROM users WHERE username = "' . $_GET["name"] . '"';
if ($result = $conn->query($sql)) {
    while ($data = $result->fetch_object()) {
        $users[] = $data;
    }
}
if(!isset($users)) {
    die();
}
$user = $users[0];
?>

<head>
    <?php include 'head.php';?>
    <title>user - webcite</title>
</head>
<body>
    <nav>
    <?php include 'nav.php';?>
    </nav>

    <main>
<?php
// foreach ($users as $user) {
    echo "<article>";
    echo "username: " . $user->username;
    echo "<br/>";
    echo "password: " . $user->password;
    echo "</article>";
// }
?>
    </main>

    <footer>
    <?php include 'foot.php';?>
    </footer>
  </body>

</html>