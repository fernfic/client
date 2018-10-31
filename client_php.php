<?php
require_once('lib/nusoap.php');

$client = new nusoap_client("https://testselect.herokuapp.com/server.php?wsdl");

//----------------pre test--------------------------//
// $air_data = array('room' => '80', 'time' => '12-09-2016 05:00', 'temp' => 22.5, 'humidity' => 10.12);
// $result = $client->call("set_data", array("data" => $air_data));
$result = $client->call("get_data", array("data" => "01"));

//----------------test1------------------------------//
$result = $client->call("get_user", array("data" => "01"));

//-----------------test2-----------------------------//
// $kerry = array('name' => 'fern', 'addr' => '123', 'weight' => '22.5');
// $result = $client->call("send_kerry", array("data" => $kerry));
// $update = array('id' => '11', 'name' => 'Pee');
// $result = $client->call("update_kerry", array("data" => $update));
$result = $client->call("get_kerry", array("data" => '01'));

print_r($result);


?>