import yaml

def returnTableYaml(filePath):
    with open(filePath) as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        for k, v in doc.items():
            if k == 'table':
                table_dict = v
    return table_dict

def to_camelcase(s):
    return ''.join(word.title() for word in s.split('_'))

def createMigrationFile(table, attributes):
    file = open("mig.php", "a")
    file.write("<?php\n")
    file.write("use Illuminate\Support\Facades\Schema;\n")
    file.write("use Illuminate\Database\Schema\Blueprint;\n")
    file.write("use Illuminate\Database\Migrations\Migration;\n")
    file.write("\n")
    camelTable = to_camelcase(table)
    file.write("class Create" + camelTable + "Table extends Migration\n")
    file.write("{\n")
    file.write("public function up() {\n")
    file.write("""Schema::create('flights', function (Blueprint $table) {\n""")
    for attribute, typ in attributes.items():
        if attribute == "id" and typ[0] == "integer":
            file.write("""$table->increments('id');\n""")
        else:
            file.write("""$table->""" + typ[0] + """("{}");\n""".format(attribute))
    file.write("$table->timestamps();\n")
    file.write("});\n")
    file.write("}\n")
    file.write("public function down() {\n")
    file.write("""Schema::drop("{}");\n""".format(table))
    file.write("}\n")
    file.write("}\n")
