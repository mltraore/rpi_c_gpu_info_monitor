import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14
import QtCharts 2.14


ApplicationWindow {
    id: root
    visible: true
    width: 1000
    height: 725
    title: qsTr("Remote RPi CPU&GPU info monitor")
    color:  "#E5E4E2"    //"#001d28"
    property real cp: 0.0
    property real gp: 0.0
    property int  carm : 0
    property int  ccore: 0
    property int  ch264: 0
    property int  cuart: 0
    property int  cpwm : 0
    property int  chdmi: 0

    property int  mcpu : 0
    property int  mgpu : 0

    property var  coh264: ""
    property var  compg2 : ""
    property var  compg4 : ""
    property var  cowvc1 : ""
    property var  comjpg : ""

    property real vcore   : 0.0
    property real sdram_c : 0.0
    property real sdram_i : 0.0
    property real sdram_p : 0.0

    property real  cp_t : 0.0
    property real  gp_t : 0.0

    Rectangle{
        id: graphId
        x:20 ; y:20
        width: parent.width*60/100
        height: parent.height - 40
        radius: 10

        /*gradient: Gradient {
                GradientStop { position: 0.0; color: "#006d93";}
                GradientStop { position: 0.5; color: "#003345";}
                GradientStop { position: 1.0; color: "#00161e";}
        }*/

        color: "white"

        border {
             //color: "black";
            color: "#D4D4D4"
        }


        Frame{
          id: graphFrame
          x: parent.x
          y: parent.y + parent.height/3
          width: parent.width - 10
          height: parent.height/2
          padding: -9

          background: Rectangle {
                    color: "transparent"
                    //color: Qt.rgba(0.694, 0.694, 0.694, 0.1)
                    border.color: "transparent"
                    radius: 2
          }


          anchors.bottom: parent.bottom
          anchors.horizontalCenter: parent.horizontalCenter



          ChartView {
                  //backgroundColor: Qt.rgba(0.694, 0.694, 0.694, 0.1)//"transparent"

                  id: chartSignal1
                  backgroundColor: "transparent"
                  anchors.fill: parent
                  antialiasing: true
                  animationOptions: ChartView.SeriesAnimations
                  legend.visible: true
                  legend.markerShape: Legend.MarkerShapeFromSeries
                  legend.alignment: Qt.AlignTop


                  ValueAxis {
                     id: axisX
                     visible: true
                     //gridVisible: false
                  }

                  ValueAxis {
                     id: axisY
                     visible: true
                     //gridVisible: chart1X.gridVisible
                   }

                   LineSeries {
                        id: cpuSignal
                        name: "CPU Temp °C"
                        color: "blue"
                        axisX: axisX
                        axisY: axisY
                    }

                   LineSeries {
                        id: gpuSignal
                        name: "GPU Temp °C"
                        color: "green"
                        axisX: axisX
                        axisY: axisY
                    }

                   Timer{
                       interval: 10000
                       repeat: true
                       running: true
                       onTriggered: updateSignal()
                   }
          }
        }


        Row{
            spacing: graphId.width*18/100
            x: graphId.width*15/100  ; y: 60
            Rectangle{
                width: graphId.width*25/100
                height: graphId.width*25/100
                color: "transparent" //Qt.rgba(0.694, 0.694, 0.694, 0.1)
                radius: graphId.width*25/100
                //border.color: Qt.rgba(0.8, 0.8, 0.8, 0.2)
                border.color: Qt.rgba(0.008, 0.651, 0.902, 0.5)

             Column{
                //anchors.fill: parent
                spacing: 20
                anchors.centerIn: parent



                Text {
                    id: cpuAvg
                    text: qsTr("CPU Avg")
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Text {
                    id: cpuAvgValue
                    text: qsTr(root.cp + "  °C")
                    color: "#00A4E4"
                    font.pixelSize: 30
                    anchors.horizontalCenter: parent.horizontalCenter

                }

                Text {
                    id: cpuAvgTem
                    text: qsTr("temperature")
                    anchors.horizontalCenter: parent.horizontalCenter
                }

             }
            }

            Rectangle{
                width: graphId.width*25/100
                height: graphId.width*25/100
                color: "transparent" //Qt.rgba(0.694, 0.694, 0.694, 0.1)
                radius: graphId.width*25/100
                //border.color: Qt.rgba(0.8, 0.8, 0.8, 0.2)

                border.color: Qt.rgba(0.008, 0.651, 0.902, 0.5)

                /*   "#02A6E6"   */

                Column{
                   //anchors.fill: parent
                   spacing: 20
                   anchors.centerIn: parent



                   Text {
                       id: gpuAvg
                       text: qsTr("GPU Avg")
                       anchors.horizontalCenter: parent.horizontalCenter
                   }

                   Text {
                       id: gpuAvgValue
                       text: qsTr(root.gp + "  °C")
                       color: "#00A4E4"
                       font.pixelSize: 30
                       anchors.horizontalCenter: parent.horizontalCenter

                   }

                   Text {
                       id: gpuAvgTem
                       text: qsTr("temperature")
                       anchors.horizontalCenter: parent.horizontalCenter
                   }

                }
            }


        }

    }

    Rectangle{
        id: infoId
        x:parent.width - (width + 20) ; y:20
        width: parent.width*32/100
        height: parent.height - 40
        radius: 10

        /*
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#006d93";}
            GradientStop { position: 0.5; color: "#003345";}
            GradientStop { position: 1.0; color: "#00161e";}
            }
        */

        color: "white"

        border {
             //color: "black";
            color: "#D4D4D4"
        }






        Column{
           //anchors.fill: parent
           //anchors.centerIn: parent

           spacing: 8

           Rectangle{
            id: tempe
            //color: "lightblue"
            color: "#00A4E4"
            width: infoId.width ; height:  infoId.height*5/100
            radius: infoId.radius

            Text {
                text: qsTr("Current Temperature (°C)")
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "white"
            }
           }

           Text {
               id: tc
               text: qsTr(" cpu  :   " + root.cp_t.toFixed(1))
           }

           Text {
               id: tg
               text: qsTr(" gpu  :   " + root.gp_t.toFixed(1))
           }
           Rectangle{
             id:clock
             color: "#00A4E4"
             width: infoId.width ; height:  infoId.height*5/100
             radius: infoId.radius
             //border-bottom-left-radius: 3px;

             Text {
                 text: qsTr("Clock Frequencies(Mhz)")
                 anchors.horizontalCenter: parent.horizontalCenter
                 anchors.verticalCenter: parent.verticalCenter
                 color: "white"
             }
           }

           Text {
               id: carm
               text: qsTr(" arm    :  " + root.carm)
           }
           Text {
               id: ccore
               text: qsTr(" core   :  " + root.ccore)
           }

           Text {
               id: cuart
               text: qsTr(" uart    :   " + root.cuart)
           }

           Text {
               id: ch264
               text: qsTr(" h264  :  " + root.ch264)
           }

           Text {
               id: cpwm
               text: qsTr(" pwm  :  " + root.cpwm)
           }


           Text {
               id: chdmi
               text: qsTr(" hdmi  :  " + root.chdmi)
           }


           Rectangle{
            id: voltage
            color: "#00A4E4"
            width: infoId.width ; height:  infoId.height*5/100
            radius: infoId.radius

            Text {
                text: qsTr("Voltages (V)")
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "white"
            }
           }

           Text {
               id: vcore
               text: qsTr(" core  :     " + root.vcore)
           }
           Text {
               id: vsdram_c
               text: qsTr(" sdram_c  :  " + root.sdram_c)
           }
           Text {
               id: vsdram_i
               text: qsTr(" sdram_i   :  " + root.sdram_i)
           }
           Text {
               id: vsdram_p
               text: qsTr(" sdram_p  :  " + root.sdram_p )
           }

           Rectangle{
            id: codecs
            color: "#00A4E4"
            width: infoId.width ; height:  infoId.height*5/100
            radius: infoId.radius

            Text {
                text: qsTr("Codecs Enabled")
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "white"
            }
           }

           Text {
               //id: coh264
               text: qsTr(" h264   :    " + root.coh264)
           }

           Text {
               id: compg2
               text: qsTr(" mpg2 :    " + root.compg2)
           }

           Text {
               id: compg4
               text: qsTr(" mpg4 :    " + root.compg4)
           }
           Text {
               id: cowvc1
               text: qsTr(" wvc1  :    " + root.cowvc1)
           }

           Text {
               id: comjpg
               text: qsTr(" mjpg  :    " + root.comjpg)
           }

           Rectangle{
            id: mem
            color: "#00A4E4"
            width: infoId.width ; height:  infoId.height*5/100
            radius: infoId.radius

            Text {
                text: qsTr("Memory Allocation (MB)")
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                color: "white"
            }
           }

           Text {
               id: marm
               text: qsTr(" arm    :     " + root.mcpu)
           }

           Text {
               id: mgpu
               text: qsTr(" gpu    :     " + root.mgpu)
           }

           /*
           Text {
               id: cpuA
               text: qsTr("CPU Avg")
               anchors.horizontalCenter: parent.horizontalCenter
           }

           Text {
               id: cpuAv
               text: qsTr(root.cp + "  °C")
               color: "#00A4E4"
               font.pixelSize: 30
               anchors.horizontalCenter: parent.horizontalCenter

           }

           Text {
               id: cpuAvgTem
               text: qsTr("temperature")
               anchors.horizontalCenter: parent.horizontalCenter
           }

           */

        }
    }


    function updateSignal(){
        cpuSignal.clear()
        gpuSignal.clear()

        CPU.sig()

        var cs = CPU.sig_cpu
        var gs = CPU.sig_gpu
        var t  = CPU.sig_time


        root.coh264 = CPU.sig_coh264
        root.compg2 = CPU.sig_compg2
        root.compg4 = CPU.sig_compg4
        root.cowvc1 = CPU.sig_cowvc1
        root.comjpg = CPU.sig_comjpg

        root.cp_t = cs[cs.length-1]
        root.gp_t = gs[gs.length-1]

        root.cp = CPU.sig_cavg
        root.gp = CPU.sig_gavg

        root.carm  = Math.round(CPU.sig_carm/1000000)
        root.ccore = Math.round(CPU.sig_ccore/1000000)
        root.ch264 = Math.round(CPU.sig_ch264/1000000)
        root.cuart = Math.round(CPU.sig_cuart/1000000)
        root.cpwm  = Math.round(CPU.sig_cpwm/1000000)
        root.chdmi = Math.round(CPU.sig_chdmi/1000000)

        root.mcpu  = Math.round(CPU.sig_mcpu/1000000)
        root.mgpu  = Math.round(CPU.sig_mgpu/1000000)

        root.vcore   = CPU.sig_vcore
        root.sdram_c = CPU.sig_sdram_c
        root.sdram_i = CPU.sig_sdram_i
        root.sdram_p = CPU.sig_sdram_p


        for(var i = 0; i< cs.length; i++){
            cpuSignal.append(t[i], cs[i])
            gpuSignal.append(t[i], gs[i])
        }

        axisX.max = t[t.length-1]
        axisX.min = t[0]
        axisY.max = Math.max.apply(null, cs) + 10
        axisY.min = Math.min.apply(null, cs)

    }
}



