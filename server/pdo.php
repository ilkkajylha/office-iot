<?php
$servername = "localhost";
$username = "officeiot";
$password = "password";
$dbname = "officeiot";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // prepare sql and bind parameters
    $stmt = $conn->prepare("INSERT INTO rooms (room_number, room_status) 
    VALUES (:room_number, :room_status)");
    $stmt->bindParam(':room_number', $_GET["room_number"]);
    $stmt->bindParam(':room_status', $_GET["room_status"]);
    $stmt->execute();
}
catch(PDOException $e)
    {
    echo "Error: " . $e->getMessage();
    }
$conn = null;
?>

