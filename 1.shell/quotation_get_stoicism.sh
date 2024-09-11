#!/bin/bash
##
## FILE: quotation_get_stoicism.sh
##
## DESCRIPTION: Generates random stoicism quotation response from a free API.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: quotation_get_stoicism.sh
##

# TODO(chrisbuckleycode): Add check for jq

# Define API endpoint
API_ENDPOINT="https://api.themotivate365.com/stoic-quote"
API_KEY="my-secret-key"

# Make API call and store response in variable
response=$(curl -s -X GET \
  -H "Authorization: Bearer $API_KEY" \
  -H "Accept: application/json" \
  "$API_ENDPOINT")


# Extract author and quote from response
author=$(jq -r ".author" <<< "$response")
quote=$(jq -r ".quote" <<< "$response")

# Print author and quote
echo "Author: ${author}"
echo "Quote: ${quote}"
