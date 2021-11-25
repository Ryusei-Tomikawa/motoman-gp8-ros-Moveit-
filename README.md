## motoman-gp8-ros
このリポジトリは安川電機のmotoman-gp8をMoveit！で動かすことが可能にしている
すでにrosで制御可能なmotomanのパッケージ[ros-industrial/motoman](https://github.com/ros-industrial/motoman)
が存在するが、産業ロボットの種類によってmoveit!で制御できないロボットが存在する
その１つがmotoman-gp8であるため、このリポジトリを用いることでMoveit!で動作確認することを可能とした

## インストール方法
このリポジトリをインストールする際には、motomanのパッケージ[ros-industrial/motoman](https://github.com/ros-industrial/motoman)
をワークスペースの中に入っていることが前提である.
以下の方法でインストールすること

 ```shell
  $ cd ~/catkin_ws/src/motoman
  $ git clone https://github.com/Ryusei-Tomikawa/motoman-gp8-ros
  $ cd ../../
  $ catkin build
 ```

## 動作確認
 このリポジトリにサンプルスクリプトがあるので実際にシミュレーションで動作してみる
 
 ```shell
  $ roslaunch motoman_gp8_moveit_config demo.launch
  $ rosrun motoman_gp8_moveit_config motoman.py
 ```
これによりシミュレーションで動作が可能となる
なお、実機を用いても動作確認済である. 詳細は[motoman-gp8 Moveit!実機動作方法](http://www1.meijo-u.ac.jp/~kohara/cms/technicalreport/ros_motoman_gp8_setup)に記す
