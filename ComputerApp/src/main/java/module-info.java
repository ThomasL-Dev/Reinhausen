module com.reinhausen.computerapp {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires validatorfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires eu.hansolo.tilesfx;
    requires java.net.http;

    opens com.reinhausen.computerapp to javafx.fxml;
    exports com.reinhausen.computerapp;
    exports com.reinhausen.computerapp.Bin.Controllers;
    opens com.reinhausen.computerapp.Bin.Controllers to javafx.fxml;
}