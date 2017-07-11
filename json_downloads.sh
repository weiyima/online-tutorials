
for ((i=1;i<6;i++)); do
    curl -o "json_downloads/citibike_data_"$i".json" "https://feeds.citibikenyc.com/stations/stations.json";
    sleep 5;
done