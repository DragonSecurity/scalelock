package util

import "net/url"

func BuildVerificationURL(baseURL string, basePath string, token string, callbackURL *string) string {
	urlToConstruct := baseURL + basePath + "/verify-email"

	// We can safely ignore the error here because we are constructing the URL ourselves which is always valid.
	constructedUrl, _ := url.Parse(urlToConstruct)
	q := constructedUrl.Query()
	q.Set("token", token)

	if callbackURL != nil && *callbackURL != "" {
		q.Set("callback_url", *callbackURL)
	}

	constructedUrl.RawQuery = q.Encode()

	return constructedUrl.String()
}
