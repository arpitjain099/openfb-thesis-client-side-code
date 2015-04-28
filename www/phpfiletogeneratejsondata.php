<?php
header('Access-Control-Allow-Origin: *');


//echo $passworda;
//$device = $_GET['device'];
$m = new MongoClient();
   //echo "Connection to database successfully";
   //echo "<br>";
   // select a database
   $db = $m->temp;
   //echo "Database thesisdb selected";
   $collection = $db->completedtask;
   $collection2= $db->curr;
   $joe = $collection->find();
   $joe2 = $collection2->find();
   foreach ( $joe as $id => $value1 )
{	
	foreach($joe2 as $id2=> $value2)
  if ($value2['taskid']!=$value1['taskid'])
    echo $value2['taskid'];
    //echo "$id: ";
		    //echo json_encode($value2);

    //var_dump( $value2 );

}
   //echo $joe[0].taskid;
   
   //echo "Collection selected succsessfully";
   //$joe = $collection->findOne(array("username" => $_POST['username'],"password"=> $_POST['password']));
   //if(!$joe)echo "wrong credentials";
   //
   //else echo "user found";
//echo $result+"";

?>