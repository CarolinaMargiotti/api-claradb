from flask import jsonify

from models.database.MongoConnection import PyMongoConnection


def getFolsByStatus(equipmentList, status):
    conn = PyMongoConnection()

    condition = {
        "Equipment": {
            "$in": equipmentList
        },
        "Status": status
    }

    projection = {
        "_id": 0,
        "id": 1,
        "Title": 1,
        "Equipment": 1,
        "Issue description": 1
    }

    document = jsonify(list(conn.getDocuments("folconn", "documents", condition, projection)))

    return document


def getFolsByKeywords(equipmentList, keywords):
    conn = PyMongoConnection()

    condition = {
        "Equipment": {
            "$in": equipmentList
        },
        "Keywords": {
            "$in": keywords
        }
    }

    projection = {
        "_id": 0,
        "id": 1,
        "Title": 1,
        "Equipment": 1,
        "Issue description": 1
    }

    document = jsonify(list(conn.getDocuments("folconn", "documents", condition, projection)))

    return document


def getFolsByCategory(equipmentList, category):
    conn = PyMongoConnection()

    condition = {
        "Equipment": {
            "$in": equipmentList
        },
        "Category": category
    }

    projection = {
        "_id": 0,
        "id": 1,
        "Title": 1,
        "Equipment": 1,
        "Issue description": 1
    }

    document = jsonify(list(conn.getDocuments("folconn", "documents", condition, projection)))

    return document


def getFolsCategories(equipmentList):
    conn = PyMongoConnection()

    pipeline = [
        {
            '$match': {
                'Equipment': {
                    '$in': equipmentList
                }
            }
        },
        {
            '$group': {
                '_id': '$Category'
            }
        }
    ]

    document = list(conn.aggregate("folconn", "documents", pipeline))

    categoriesList = []

    for result in document:
        category = result["_id"]

        categoriesList.append(category)

    return jsonify(categoriesList)


def getFolsByTitle(carsList, title):
    conn = PyMongoConnection()

    condition = {
        "Equipment": {
            "$in": carsList
        },
        "Title": {"$regex": title}
    }

    projection = {
        "_id": 0,
        "id": 1,
        "Title": 1,
        "Equipment": 1,
        "Issue description": 1
    }

    document = jsonify(list(conn.getDocuments("folconn", "documents", condition, projection)))

    return document


def getFolFirstPage(folTitle):

    opened_pdf = PyPDF2.PdfFileReader("../resources/FOL-MUS-FATEC.pdf")
    total_pages_pdf = opened_pdf.getNumPages()

    for page_number in range(0, total_pages_pdf):

        opened_page = opened_pdf.getPage(page_number)
        print("this is page " + str(page_number))

        page_text = opened_page.extractText()
        print(page_text)

        result_search = re.search(folTitle, page_text)
        print(result_search)

        return jsonify(1)
