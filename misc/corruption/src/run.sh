sudo docker build -t corrupt .
sudo docker run -d -p 2000:9999 corrupt
