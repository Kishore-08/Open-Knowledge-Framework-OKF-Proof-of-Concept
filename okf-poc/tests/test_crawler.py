#New Page
assert result.changed == 1
assert result.changed_urls == [url]

#Same content
assert second.changed == 0
assert second.unchanged == 1

#changed content
assert second.changed == 1
assert url in second.changed_urls

#deleted content
assert result.deleted == 1
assert result.deleted_urls == ["/page-b"]