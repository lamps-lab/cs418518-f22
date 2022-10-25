<?php
require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->build();

$params = [
	'index' => 'my_index',
	'id'    => 'my_id'
];

$response = $client->get($params);
echo "<h3>GET response </h3>";
print_r($response);
echo "<br>";

?>
