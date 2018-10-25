<?php
require_once('lib/nusoap.php');

// $client = new nusoap_client("https://testselect-wolfbit.c9users.io/server.php?wsdl");

$client = new nusoap_client("https://testselect.herokuapp.com/server.php?wsdl");

$data = array('room' => '01', 'time' => '12-09-2016 05:00', 'temp' => 22.5, 'humidity' => 10.12);
$kerry1 = array('name' => 'fern', 'addr' => '123', 'weight' => '22.5');
$kerry2 = array('name' => 'pee', 'addr' => '345', 'weight' => '50');
// $result = $client->call("send_kerry", array("data" => $kerry2));
// $result = $client->call("update_kerry", array("data" => $kerry2));
$result = $client->call("get_kerry", array("name" => "fern"));
print_r($result);

//function defination to convert array to xml
function array_to_xml($array, &$xml_user_info) {
    foreach($array as $key => $value) {
        if(is_array($value)) {
            if(!is_numeric($key)){
                $subnode = $xml_user_info->addChild("$key");
                array_to_xml($value, $subnode);
            }else{
                $subnode = $xml_user_info->addChild("item$key");
                array_to_xml($value, $subnode);
            }
        }else {
            $xml_user_info->addChild("$key",htmlspecialchars("$value"));
        }
    }
}

//creating object of SimpleXMLElement
$xml_user_info = new SimpleXMLElement("<?xml version=\"1.0\"?><data></data>");

//function call to convert array to xml
array_to_xml($result,$xml_user_info);

//saving generated xml file
$xml_file = $xml_user_info->asXML('kerryData.xml');

?>