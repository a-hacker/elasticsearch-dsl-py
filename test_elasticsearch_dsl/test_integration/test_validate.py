from elasticsearch_dsl.search import Search, Q


def test_validate_succeeds(data_client):
    s = Search(using=data_client).index('git')
    assert s.validate().valid


def test_validate_bad_query(data_client, mocker):
    s = Search(using=data_client).index('git').filter(Q())
    assert not s.validate().valid


def test_validate_explain(data_client):
    s = Search(using=data_client).index('git').filter(~Q('exists', field='parent_shas'))
    assert 'explanations' in s.validate()
