<<<<<<< HEAD
<html>
<body>

<form action="Hello.php" method="get">
First Name: <input type="text" name="fname">
<br>
Last Name: <input type="text" name="lname">
<br>
Age: <input type="number" name="age">
<br>


<input type="submit">
</form>


<?php
if ($_GET["fname"] == "dor") {
echo "Hello Boss!";

}

?>
<br>

Your Last name:<?php echo $_GET["lname"] ?>

</body>
</html>
=======
<?php
echo "COVID19!";

?>
>>>>>>> 4e2447fe161b2901047c2b146dc35d68d48cf14f
