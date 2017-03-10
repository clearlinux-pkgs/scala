PKG_NAME := scala
URL := https://github.com/scala/scala/archive/v2.11.8.tar.gz
ARCHIVES := https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/943cd5c8802b2a3a64a010efb86ec19bac142e40/lib/ant-contrib.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/ddd7d5398733c4fbbb8355c049e258d47af636cf/lib/forkjoin.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/3fc1e35ca8c991fc3488548f7a276bd9053c179d/lib/ant/ant-dotnet-1.0.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/7b456ca6b93900f96e58cc8371f03d90a9c1c8d1/lib/ant/ant.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/7e50e3e227d834695f1e0bf018a7326e06ee4c86/lib/ant/maven-ant-tasks-2.1.1.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/2c61d6e9a912b3253194d5d6d3e1db7e2545ac4b/lib/ant/vizant.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/981392dbd1f727b152cd1c908c5fce60ad9d07f7/test/files/lib/enums.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/02fe2ed93766323a13f22c7a7e2ecdcd84259b6c/test/files/lib/annotations.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/b1ec8a095cec4902b3609d74d274c04365c59c04/test/files/lib/genericNest.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/346d3dff4088839d6b4d163efa2892124039d216/test/files/lib/jsoup-1.3.1.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/3794ec22d9b27f2b179bd34e9b46db771b934ec3/test/files/lib/macro210.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/be8454d5e7751b063ade201c225dcedefd252775/test/files/lib/methvsfield.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/cd33e0a0ea249eb42363a2f8ba531186345ff68c/test/files/lib/nest.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/e737b123d31eede5594ceda07caafed1673ec472/test/files/codelib/code.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/1b11ac773055c1e942c6b5eb4aabdf02292a7194/test/files/speclib/instrumented.jar . \
	https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/a1883f4304d5aa65e1f6ee6aad5900c62dd81079/tools/push.jar . \
    http://repo1.maven.org/maven2/biz/aQute/bnd/1.50.0/bnd-1.50.0.pom . \
	http://repo1.maven.org/maven2/biz/aQute/bnd/1.50.0/bnd-1.50.0.jar .

include ../common/Makefile.common
