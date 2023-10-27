# Princípios SOLID em Python

Este projeto demonstra a aplicação dos cinco princípios SOLID em código Python. Cada princípio é explicado e ilustrado com exemplos.

## Princípio da Responsabilidade Única (SRP)

Suponha que você esteja desenvolvendo um sistema de gerenciamento de pedidos. O SRP sugere que você crie classes com responsabilidades bem definidas. Uma possível classe com responsabilidade única poderia ser a `Order` para representar um pedido e outra classe `OrderPrinter` para lidar com a impressão de detalhes do pedido. Assim, a `Order` é responsável apenas por representar os dados do pedido, enquanto a `OrderPrinter` cuida exclusivamente da lógica de impressão.

## Princípio da Abertura/Fechamento (OCP)

Suponha que você tenha um sistema de geração de relatórios e deseja adicionar a capacidade de exportar relatórios em diferentes formatos, como PDF, CSV e HTML. Para seguir o OCP, você criaria uma interface `ReportExporter` com métodos para exportar relatórios e, em seguida, implementaria classes concretas como `PdfExporter`, `CsvExporter`, e `HtmlExporter` que se encaixariam nessa interface. Dessa forma, você pode estender o sistema para suportar novos formatos de exportação sem modificar o código existente.

## Princípio da Substituição de Liskov (LSP)

Suponha que você tenha uma hierarquia de classes que representam formas geométricas, como `Circle` (círculo) e `Rectangle` (retângulo), e todas elas herdam de uma classe base `Shape`. O LSP exige que métodos que operam em objetos `Shape` também funcionem corretamente com objetos de subclasse, como `Circle` e `Rectangle`, sem introduzir erros. Por exemplo, métodos que calculam a área de uma forma devem funcionar igualmente bem para qualquer subclasse de `Shape`.

## Princípio da Segregação de Interfaces (ISP)

Imagine que você esteja criando uma interface `Worker` para representar trabalhadores, e você tem métodos como `work()` e `takeBreak()`. No entanto, alguns tipos de trabalhadores, como robôs, não tiram pausas. Para aplicar o ISP, você pode criar interfaces mais específicas, como `Workable` e `Breakable`, e, em seguida, suas classes de trabalhadores podem implementar apenas as interfaces relevantes para suas capacidades.

## Princípio da Inversão de Dependência (DIP)

Suponha que você tenha um sistema de envio de e-mails e um sistema de notificação de clientes. Para aplicar o DIP, você pode criar uma abstração, como uma interface `NotificationService`, que define métodos para enviar notificações. Em seguida, as classes do sistema de notificação dependem dessa interface. Se, no futuro, você desejar substituir o serviço de envio de e-mails por um serviço de mensagens push, basta criar uma nova classe que implemente a mesma interface, e as classes de notificação não precisarão ser alteradas.

Cada exemplo apresentado neste projeto demonstra a aplicação prática desses princípios em código Python.

