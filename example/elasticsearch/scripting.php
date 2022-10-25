<?php
require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->build();

$params = [
	'index' => 'test',
	'id'    => '1'
];

echo "<h3>GET index </h3>";
$response = $client->get($params);
print_r($response);

$params = [
   'index' => 'test',
   'id'    => '1',
   'body'  => [
        'script' => [
            'source' => 'ctx._source.counter += params.count',
            'params' => [ 'count' => 4 ]
         ]
    ]
];

echo "<h3>Update index</h3>";
$response=$client->update($params);
print_r($response);

$params = [
	'index' => 'test',
	'id'    => '1'
];

$response = $client->get($params);
echo "<h3>GET index </h3>";
print_r($response);
?>
