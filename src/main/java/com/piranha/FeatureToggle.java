package com.piranha;

public class FeatureToggle {

  public String get(String requestNumberPrefix, String request) {
    if (Boolean.parseBoolean(TenantConfiguration.get(TenantConfigurationKey.FEATURE_SEQUENTIAL_NUMBERS_FOR_WARRANTY))) {
      return "true";
    }
    return "false";
  }

}
