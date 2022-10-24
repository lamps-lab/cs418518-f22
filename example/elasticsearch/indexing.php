<?php
require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->build();

$params = [
  'index' => 'my_index',
  'id'    => 'my_id',
  'body'  => ['testField' => 'abc']
];

$response = $client->index($params);
echo "<h3>We indexed these.</h3>";
print_r($params);
echo "<h3><Response/h3>";
print_r($response);
echo "<br>";
?>


