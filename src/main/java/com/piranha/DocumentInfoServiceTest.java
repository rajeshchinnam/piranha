package com.piranha;

public class DocumentInfoServiceTest {

  void shouldGetRandomValueIfFeatureIsDisabled() {

    when("true").thenReturn("false");
    System.out.println("Hello World");
  }
}
