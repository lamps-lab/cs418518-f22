<?php
require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->build();

$params = [
  'index' => 'test',
  'id'    => '1',
  'body'  => ['counter' => 1]
];

$response = $client->index($params);
echo "<h3>We indexed these.</h3>";
print_r($params);
echo "<br>";
?>
