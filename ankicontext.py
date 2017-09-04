import aqt
from anki.hooks import addHook


# User defined constants
KANJI_FIELD = 'kanji'  # Set to something other than '' to limit to field
KANJI_TAG = 'kanji'  # Set to something other than '' to limit to a tag


def lookup_kanji(kanji):
    browser = aqt.dialogs.open("Browser", aqt.mw)
    tag = ''
    if KANJI_TAG:
        tag = u'tag:"{kanji_tag}"'.format(kanji_tag=KANJI_TAG)
    join_string = ' or '
    if KANJI_FIELD:
        join_string = ' or {field}:'.format(field=KANJI_FIELD)
    query = u'{tag} ({kanji_field}{kanji_query})'.format(
        tag=tag,
        kanji_field='{}:'.format(KANJI_FIELD) if KANJI_FIELD else '',
        kanji_query=join_string.join(kanji),
    ).strip()
    browser.form.searchEdit.lineEdit().setText(query)
    browser.onSearch()


def add_context_actions(view, menu):
    selection = view.page().selectedText()
    if not selection:
        return

    kanji_lookup_item = menu.addAction('Search for kanji in card browser')
    kanji_lookup_item.triggered.connect(lambda: lookup_kanji(selection))


addHook('AnkiWebView.contextMenuEvent', add_context_actions)
