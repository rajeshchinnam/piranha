package com.piranha;

public enum TenantConfigurationKey {

  FEATURE_SEQUENTIAL_NUMBERS_FOR_WARRANTY("feature.2024.09.gpd.35102-warranty-sequence-number");

  private final String value;

  TenantConfigurationKey(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

}
