#!/usr/bin/env python3
"""
Latency Adder Tool - Add artificial latency/delay to network requests or commands.
"""

import time
import sys
import argparse
import subprocess
from datetime import datetime


def add_latency(delay_ms):
    """Add artificial latency by sleeping for the specified milliseconds."""
    delay_seconds = delay_ms / 1000.0
    time.sleep(delay_seconds)


def execute_with_latency(command, delay_ms, verbose=False):
    """
    Execute a command with added latency before execution.
    
    WARNING: This function uses shell=True for convenience, which can be a security
    risk if the command contains untrusted input. Only use with trusted commands.
    """
    if verbose:
        print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] Adding {delay_ms}ms latency before execution...")
    
    add_latency(delay_ms)
    
    if verbose:
        print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] Executing command: {command}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        
        execution_time = (time.time() - start_time) * 1000
        
        if verbose:
            print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] Command completed in {execution_time:.2f}ms")
            print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] Total time (including latency): {execution_time + delay_ms:.2f}ms")
        
        if result.stdout:
            print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='', file=sys.stderr)
        
        return result.returncode
    
    except (subprocess.SubprocessError, FileNotFoundError, PermissionError) as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def benchmark_latency(iterations=10, delay_ms=100):
    """Benchmark latency addition accuracy."""
    print(f"Benchmarking latency addition with {iterations} iterations of {delay_ms}ms delay...")
    
    total_time = 0
    results = []
    
    for i in range(iterations):
        start = time.time()
        add_latency(delay_ms)
        elapsed = (time.time() - start) * 1000
        results.append(elapsed)
        total_time += elapsed
        print(f"Iteration {i+1}: {elapsed:.3f}ms")
    
    avg_time = total_time / iterations
    min_time = min(results)
    max_time = max(results)
    
    print(f"\nResults:")
    print(f"  Average: {avg_time:.3f}ms")
    print(f"  Min: {min_time:.3f}ms")
    print(f"  Max: {max_time:.3f}ms")
    print(f"  Target: {delay_ms}ms")
    print(f"  Accuracy: {(avg_time/delay_ms)*100:.2f}%")


def main():
    """Main entry point for the latency adder tool."""
    parser = argparse.ArgumentParser(
        description='Latency Adder - Add artificial latency to commands or benchmark delays',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --delay 100 --command "echo Hello"
  %(prog)s -d 500 -c "curl https://example.com"
  %(prog)s --benchmark --iterations 10 --delay 100
  %(prog)s -b -i 5 -d 250
        """
    )
    
    parser.add_argument(
        '-d', '--delay',
        type=float,
        default=100,
        help='Latency delay in milliseconds, supports fractional values (default: 100)'
    )
    
    parser.add_argument(
        '-c', '--command',
        type=str,
        help='Command to execute with added latency (WARNING: only use trusted commands)'
    )
    
    parser.add_argument(
        '-b', '--benchmark',
        action='store_true',
        help='Run latency benchmark mode'
    )
    
    parser.add_argument(
        '-i', '--iterations',
        type=int,
        default=10,
        help='Number of iterations for benchmark (default: 10)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    if args.benchmark:
        benchmark_latency(args.iterations, args.delay)
        return 0
    
    if args.command:
        return execute_with_latency(args.command, args.delay, args.verbose)
    
    # Interactive mode - just add delay
    if args.verbose:
        print(f"Adding {args.delay}ms latency...")
    
    start = time.time()
    add_latency(args.delay)
    elapsed = (time.time() - start) * 1000
    
    if args.verbose:
        print(f"Latency added: {elapsed:.3f}ms")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
