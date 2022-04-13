<?php
    if($_SERVER["REQUEST_METHOD"]==POST){
        $connection=mysqli_connect("localhost", "grace", "Gra814me13%");
    


    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }
      echo "Connected successfully";
    }

?>