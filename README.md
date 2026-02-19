# Latency Adder

A Python tool for adding artificial latency/delays to commands and benchmarking latency accuracy.

## Features

- ⏱️ **Add Artificial Latency**: Simulate network delays for testing
- 🚀 **Command Execution**: Execute commands with pre-execution delays
- 📊 **Benchmark Mode**: Verify latency addition accuracy
- 🔧 **Flexible Configuration**: Support for fractional millisecond delays
- 📝 **Verbose Mode**: Detailed timing information

## Installation

No installation required! Just make sure you have Python 3 installed.

```bash
chmod +x sigma.py
```

## Usage

### Basic Latency Addition

Add a simple delay:

```bash
python3 sigma.py -d 200 -v
```

### Execute Command with Latency

Run a command with added latency:

```bash
python3 sigma.py -d 100 -c "echo Hello World" -v
```

### Benchmark Mode

Test the accuracy of latency addition:

```bash
python3 sigma.py -b -i 10 -d 100
```

## Command Line Options

- `-d, --delay`: Latency delay in milliseconds (supports fractional values, default: 100)
- `-c, --command`: Command to execute with added latency (⚠️ WARNING: only use trusted commands)
- `-b, --benchmark`: Run latency benchmark mode
- `-i, --iterations`: Number of iterations for benchmark (default: 10)
- `-v, --verbose`: Enable verbose output
- `-h, --help`: Show help message

## Examples

```bash
# Add 500ms latency before executing curl
python3 sigma.py -d 500 -c "curl https://example.com"

# Benchmark with 5 iterations of 250ms delay
python3 sigma.py -b -i 5 -d 250

# Simple delay with verbose output
python3 sigma.py -d 100 -v

# Execute a test command with detailed timing
python3 sigma.py -d 50.5 -c "echo 'Testing'" -v
```

## Use Cases

- **Performance Testing**: Simulate network latency in testing environments
- **Timeout Testing**: Verify timeout handling in applications
- **Load Testing**: Add realistic delays to stress tests
- **Development**: Test application behavior under slow network conditions

## Security Note

⚠️ The command execution feature uses `shell=True` for convenience. Only use with trusted commands to avoid security risks.

## Requirements

- Python 3.x
- No external dependencies required

## License

This is a testing/demonstration tool.
