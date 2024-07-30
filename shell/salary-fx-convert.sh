#!/bin/bash
##
## FILE: salary-fx-convert.sh
##
## DESCRIPTION: Displays table of salary currency conversions.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: salary-fx-convert.sh
##

# This script produces a table of static local currency monthly salary vs equivalent home currency annual salary.
# Currencies and base values are configurable as variables.
# Future idea: tax calculations

# API endpoint URL
api_url="https://api.exchangerate-api.com/v4/latest/EUR"

# Set the base currency and target currency
# Two values are obtained and usually target_currency = 1 but not always (e.g. APIs showing rates vs a third-country currency)
base_currency="HKD"
target_currency="EUR"

# Retrieve JSON response from the API endpoint
json_response=$(curl -s "$api_url")

# Extract the exchange rates for the base currency and target currency from the JSON response using jq
base_rate=$(echo "$json_response" | jq -r ".rates.\"$base_currency\"")
target_rate=$(echo "$json_response" | jq -r ".rates.\"$target_currency\"")

# Calculate the conversion rate
conversion_rate=$(bc <<< "scale=8; $base_rate / $target_rate")

# Define the values for the "Target currency per month" column
base_per_month_values=(20000 25000 30000 35000 40000 45000 50000 55000 60000 65000 70000 75000 80000)

# Calculate the "Target currency per year" values based on the exchange rates and "Base currency per month" values
calculate_target_per_year() {
  local base_per_month="$1"
  local target_per_year=$(bc <<< "scale=2; $base_per_month * 12 / $conversion_rate")
  echo "$target_per_year"
}

# Generate the ASCII table
generate_ascii_table() {
  local header1="$base_currency (per month)"
  local header2="$target_currency (per year)"

  printf "| %-25s | %-25s |\n" "$header1" "$header2"
  printf "|---------------------------+---------------------------|\n"

  for base_value in "${base_per_month_values[@]}"; do
    local target_value=$(calculate_target_per_year "$base_value")
    printf "| %-25s | %-25s |\n" "$base_value" "$target_value"
  done
}

# Call the function to generate the ASCII table
generate_ascii_table
