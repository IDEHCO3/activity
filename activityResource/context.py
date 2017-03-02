
def addContextInHeader(url, response):
    link = ' <'+url+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\"'
    if "Link" not in response:
        response['Link'] = link
    else:
        response['Link'] += ", " + link
    return response


context = {
    "@context": {
        "iriActor": {
            "@id": "http://schema.org/actor",
            "@type": "@id"
        },
        "iriAction": {
            "@id": "http://schema.org/action",
            "@type": "@id"
        },
        "iriObject": {
            "@id": "http://schema.org/object",
            "@type": "@id"
        },
        "iriObjectTarget": {
            "@id": "http://schema.org/target",
            "@type": "@id"
        }
    }
}