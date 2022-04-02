

CREATE TABLE "ContentCheck" (
	contains_regexp TEXT, 
	minimum_line_number INTEGER, 
	maximum_line_number INTEGER, 
	PRIMARY KEY (contains_regexp, minimum_line_number, maximum_line_number)
);

CREATE TABLE "DataPackage" (
	name TEXT NOT NULL, 
	download_url TEXT, 
	license TEXT, 
	title TEXT, 
	description TEXT, 
	conforms_to TEXT, 
	conforms_to_schema TEXT, 
	conforms_to_class TEXT, 
	version TEXT, 
	language TEXT, 
	publisher TEXT, 
	issued DATETIME, 
	created_by TEXT, 
	created_on DATETIME, 
	status TEXT, 
	deprecated BOOLEAN, 
	compression VARCHAR(5), 
	was_derived_from TEXT, 
	page TEXT, 
	resources TEXT, 
	parent TEXT, 
	alternate_parents TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY(parent) REFERENCES "DataPackage" (name)
);

CREATE TABLE "DataResource" (
	name TEXT NOT NULL, 
	download_url TEXT, 
	license TEXT, 
	conforms_to TEXT, 
	conforms_to_schema TEXT, 
	conforms_to_class TEXT, 
	version TEXT, 
	language TEXT, 
	publisher TEXT, 
	issued DATETIME, 
	created_by TEXT, 
	created_on DATETIME, 
	status TEXT, 
	deprecated BOOLEAN, 
	compression VARCHAR(5), 
	was_derived_from TEXT, 
	page TEXT, 
	path TEXT, 
	title TEXT, 
	description TEXT, 
	format TEXT, 
	media_type TEXT, 
	encoding TEXT, 
	bytes INTEGER, 
	hash TEXT, 
	md5 TEXT, 
	sha256 TEXT, 
	dialect TEXT, 
	parent TEXT, 
	alternate_parents TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY(parent) REFERENCES "DataResource" (name)
);

CREATE TABLE "FormatDialect" (
	comment_prefix TEXT, 
	delimiter TEXT, 
	double_quote TEXT, 
	header TEXT, 
	quote_char TEXT, 
	PRIMARY KEY (comment_prefix, delimiter, double_quote, header, quote_char)
);

CREATE TABLE "RulePostcondition" (
	format TEXT, 
	conforms_to TEXT, 
	compression VARCHAR(5), 
	keywords TEXT, 
	PRIMARY KEY (format, conforms_to, compression, keywords)
);

CREATE TABLE "RulePrecondition" (
	basename_regexp TEXT, 
	dirname_regexp TEXT, 
	path_regexp TEXT, 
	final_suffix TEXT, 
	has_suffix TEXT, 
	has_content TEXT, 
	PRIMARY KEY (basename_regexp, dirname_regexp, path_regexp, final_suffix, has_suffix, has_content)
);

CREATE TABLE "Rule" (
	preconditions TEXT, 
	postconditions TEXT, 
	"DataPackage_name" TEXT, 
	PRIMARY KEY (preconditions, postconditions, "DataPackage_name"), 
	FOREIGN KEY("DataPackage_name") REFERENCES "DataPackage" (name)
);

CREATE TABLE "DataPackage_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "DataPackage" (name)
);

CREATE TABLE "DataPackage_test_roles" (
	backref_id TEXT, 
	test_roles VARCHAR(15), 
	PRIMARY KEY (backref_id, test_roles), 
	FOREIGN KEY(backref_id) REFERENCES "DataPackage" (name)
);

CREATE TABLE "DataResource_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "DataResource" (name)
);

CREATE TABLE "DataResource_test_roles" (
	backref_id TEXT, 
	test_roles VARCHAR(15), 
	PRIMARY KEY (backref_id, test_roles), 
	FOREIGN KEY(backref_id) REFERENCES "DataResource" (name)
);
